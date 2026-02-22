#!/usr/bin/env python3
"""Deterministic refinement kernel.

This is a minimal orchestration layer that enforces:
- Planner -> Writer -> Critic sequencing
- Iteration caps
- Deterministic evaluation gates (per evals/*.yaml)
- State persistence to state/ledger.json and state/metrics.json
- Guardrails: immutable governance files, heading preservation, diff-size cap

The kernel is sovereign: it controls transitions and stop conditions.
Roles are non-autonomous: role outputs are provided via files.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import json
import os
import re
import subprocess
import sys
import time as _time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, RootModel, ValidationError, field_validator


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "state" / "ledger.json"
METRICS_PATH = REPO_ROOT / "state" / "metrics.json"
VERSION_MAP_PATH = REPO_ROOT / "state" / "version_map.json"
ROADMAP_PATH = REPO_ROOT / "ROADMAP.md"
EVAL_CHAPTER_QUALITY_PATH = REPO_ROOT / "evals" / "chapter-quality.yaml"
EVAL_STYLE_GUARD_PATH = REPO_ROOT / "evals" / "style-guard.yaml"
EVAL_DRIFT_DETECTION_PATH = REPO_ROOT / "evals" / "drift-detection.yaml"

IMMUTABLE_GOVERNANCE_FILES = {"AGENTS.md", "CONSTITUTION.md"}


try:
    from llm_client import LLMClient, LLMClientError, LLMUsage, Provider
except Exception:  # pragma: no cover
    # Kernel can run in file-driven mode without any LLM wiring.
    LLMClient = None  # type: ignore[assignment]
    LLMClientError = RuntimeError  # type: ignore[assignment]
    Provider = str  # type: ignore[assignment]

    @dataclass(frozen=True)
    class LLMUsage:  # type: ignore[no-redef]
        prompt_tokens: int = 0
        completion_tokens: int = 0


class KernelError(RuntimeError):
    pass


def _vprint(verbose: bool, message: str) -> None:
    if not verbose:
        return
    sys.stderr.write(message.rstrip() + "\n")
    try:
        sys.stderr.flush()
    except Exception:
        pass


@dataclass(frozen=True)
class LLMConfig:
    enabled: bool
    provider: Provider
    model: str
    base_url: str | None
    api_key_env: str
    timeout_s: int


@dataclass
class LLMRun:
    client: Any
    usage: Any


class KernelCLIArgsPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    chapter_id: str | None = None
    list_chapters: bool = False
    io_dir: Path
    max_iterations: int
    max_diff_ratio: float
    max_drift_score: float
    require_two_consecutive_passes: bool | None = None
    commit: bool = False
    verbose: bool = False
    llm: bool = False
    llm_provider: str
    llm_model: str
    llm_base_url: str | None = None
    llm_api_key_env: str
    llm_timeout_s: int


@dataclass(frozen=True)
class KernelCLIArgsTransit:
    payload: KernelCLIArgsPayload

    @classmethod
    def from_namespace(cls, args: argparse.Namespace) -> "KernelCLIArgsTransit":
        return cls(
            payload=KernelCLIArgsPayload.model_validate(
                {
                    "chapter_id": str(args.chapter_id) if args.chapter_id is not None else None,
                    "list_chapters": bool(args.list_chapters),
                    "io_dir": Path(args.io_dir),
                    "max_iterations": int(args.max_iterations),
                    "max_diff_ratio": float(args.max_diff_ratio),
                    "max_drift_score": float(args.max_drift_score),
                    "require_two_consecutive_passes": args.require_two_consecutive_passes,
                    "commit": bool(args.commit),
                    "verbose": bool(args.verbose),
                    "llm": bool(args.llm),
                    "llm_provider": str(args.llm_provider),
                    "llm_model": str(args.llm_model),
                    "llm_base_url": str(args.llm_base_url) if args.llm_base_url else None,
                    "llm_api_key_env": str(args.llm_api_key_env),
                    "llm_timeout_s": int(args.llm_timeout_s),
                }
            )
        )


class PlannerInputPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    chapter_id: str
    chapter_content: str
    quality_metrics: dict[str, Any] = Field(default_factory=dict)
    previous_critic_feedback: dict[str, Any] | None = None
    chapter_hypothesis: str


class ChapterTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class RoadmapTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class WriterOutputPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class PromptTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class LLMJSONResponseTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class LLMJSONObjectTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str
    start_index: int
    end_index: int


class LLMNormalizedJSONTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str

    @field_validator("text")
    @classmethod
    def _validate_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("normalized LLM JSON response text must not be empty")
        return value


class LLMJSONObjectMappingPayload(RootModel[dict[str, Any]]):
    pass


class YAMLTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class CriticEvalInputsPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    chapter_quality: str
    style_guard: str
    drift_detection: str


class LedgerChapterPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    path: str
    status: str | None = None
    lifecycle: str | None = None
    current_iteration: int | None = 0
    quality_metrics: dict[str, Any] = Field(default_factory=dict)
    last_eval: dict[str, Any] | None = None
    stability: dict[str, Any] = Field(default_factory=dict)


class LedgerPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    chapters: dict[str, LedgerChapterPayload]


@dataclass(frozen=True)
class LedgerTransit:
    json_mapping: "JSONMappingTransit"
    raw: dict[str, Any]
    payload: LedgerPayload


class DeterministicEvalConfigPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    version: int | None = None


class ChapterQualityThresholdsPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    refine_min_total: float = 0.65


class ChapterQualityEvalConfigPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    thresholds: ChapterQualityThresholdsPayload = Field(default_factory=ChapterQualityThresholdsPayload)


class StyleGuardSentenceLengthPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    max_words: int = 28
    hard_fail_over: int = 40


class StyleGuardAdjectiveDensityPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    max_ratio: float = 0.12


class StyleGuardLimitsPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    sentence_length: StyleGuardSentenceLengthPayload = Field(default_factory=StyleGuardSentenceLengthPayload)
    adjective_density: StyleGuardAdjectiveDensityPayload = Field(default_factory=StyleGuardAdjectiveDensityPayload)


class StyleGuardForbiddenBucketPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    examples: list[str] = Field(default_factory=list)


class StyleGuardEvalConfigPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    limits: StyleGuardLimitsPayload = Field(default_factory=StyleGuardLimitsPayload)
    forbidden: dict[str, StyleGuardForbiddenBucketPayload] = Field(default_factory=dict)


@dataclass(frozen=True)
class DeterministicEvalConfigTransit:
    source_path: Path
    yaml_mapping: "YAMLMappingTransit"
    payload: DeterministicEvalConfigPayload


class YAMLMappingPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: dict[str, Any]


class JSONMappingPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: dict[str, Any]


class JSONTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class MetricsChapterPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    history: list[dict[str, Any]] = Field(default_factory=list)


class MetricsPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    chapters: dict[str, MetricsChapterPayload] = Field(default_factory=dict)


@dataclass(frozen=True)
class MetricsTransit:
    json_mapping: "JSONMappingTransit"
    raw: dict[str, Any]
    payload: MetricsPayload


class VersionMapPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    chapters: dict[str, str] = Field(default_factory=dict)
    generated_at: str | None = None


@dataclass(frozen=True)
class VersionMapTransit:
    json_mapping: "JSONMappingTransit"
    raw: dict[str, Any]
    payload: VersionMapPayload

    def with_commit(self, chapter_id: str, commit_hash: str) -> dict[str, Any]:
        next_map = dict(self.raw)
        next_chapters = dict(self.payload.chapters)
        next_chapters[chapter_id] = commit_hash
        next_map["chapters"] = next_chapters
        next_map["generated_at"] = _utc_now_iso()
        return next_map


@dataclass(frozen=True)
class PlannerInputTransit:
    chapter_id: str
    chapter_content: str
    quality_metrics: dict[str, Any]
    previous_critic_feedback: dict[str, Any] | None
    chapter_hypothesis: str

    @classmethod
    def from_payload(cls, payload: PlannerInputPayload) -> "PlannerInputTransit":
        data = payload.model_dump()
        return cls(
            chapter_id=data["chapter_id"],
            chapter_content=data["chapter_content"],
            quality_metrics=data["quality_metrics"],
            previous_critic_feedback=data["previous_critic_feedback"],
            chapter_hypothesis=data["chapter_hypothesis"],
        )

    def to_prompt_json(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=2, sort_keys=True)


class PlannerPlanPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    focus_areas: list[str]
    structural_changes: list[str]
    risk_flags: list[str]
    target_word_delta: str

    @field_validator("focus_areas")
    @classmethod
    def _validate_focus_areas(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("must not be empty")
        return value

    @field_validator("target_word_delta")
    @classmethod
    def _validate_target_word_delta(cls, value: str) -> str:
        if not re.match(r"^[+-]\d+$", value.strip()):
            raise ValueError("must look like '+400' or '-100'")
        return value.strip()


class CriticReportPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    structure_score: float = Field(ge=0.0, le=1.0)
    clarity_score: float = Field(ge=0.0, le=1.0)
    example_density: float = Field(ge=0.0, le=1.0)
    tradeoff_presence: bool
    failure_modes_present: bool
    drift_score: float = Field(ge=0.0, le=1.0)
    violations: list[str]
    decision: Literal["approve", "refine"]


@dataclass(frozen=True)
class DeterministicEvalTransit:
    chapter_quality: DeterministicEvalConfigTransit
    style_guard: DeterministicEvalConfigTransit
    drift_detection: DeterministicEvalConfigTransit


@dataclass(frozen=True)
class DeterministicEvalRulesTransit:
    chapter_quality: ChapterQualityEvalConfigPayload
    style_guard: StyleGuardEvalConfigPayload


@dataclass(frozen=True)
class OtherChapterTextTransit:
    chapter_id: str
    chapter_text: "ChapterTextTransit"


@dataclass(frozen=True)
class RoadmapTextTransit:
    source_path: Path
    raw_text: str
    payload: RoadmapTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class ChapterTextTransit:
    source_path: Path
    raw_text: str
    payload: ChapterTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class WriterOutputTransit:
    source_path: Path
    raw_text: str
    payload: WriterOutputPayload

    def to_markdown(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class PromptTextTransit:
    source_path: Path
    raw_text: str
    payload: PromptTextPayload

    def to_prompt(self) -> str:
        return self.payload.text.strip() + "\n"


@dataclass(frozen=True)
class LLMJSONResponseTextTransit:
    payload: LLMJSONResponseTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class LLMJSONObjectTextTransit:
    response_text: LLMJSONResponseTextTransit
    payload: LLMJSONObjectTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class LLMNormalizedJSONTextTransit:
    response_text: LLMJSONResponseTextTransit
    payload: LLMNormalizedJSONTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class LLMJSONObjectMappingTransit:
    object_text: LLMJSONObjectTextTransit
    payload: LLMJSONObjectMappingPayload

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.root


@dataclass(frozen=True)
class CriticEvalInputsTransit:
    payload: CriticEvalInputsPayload
    chapter_quality: YAMLTextTransit
    style_guard: YAMLTextTransit
    drift_detection: YAMLTextTransit


@dataclass(frozen=True)
class OtherChaptersTransit:
    entries: tuple[OtherChapterTextTransit, ...]

    def as_mapping(self) -> dict[str, str]:
        return {entry.chapter_id: entry.chapter_text.to_text() for entry in self.entries}


@dataclass(frozen=True)
class MetricsHistoryTransit:
    iteration: int
    critic: CriticReport
    deterministic_eval: DeterministicEval
    diff_ratio: float

    def to_metrics_entry(self) -> dict[str, Any]:
        return {
            "timestamp": _utc_now_iso(),
            "iteration": self.iteration,
            "critic": dataclasses.asdict(self.critic),
            "deterministic": {
                "passed": self.deterministic_eval.passed,
                "drift_score": self.deterministic_eval.drift_score,
                "similarity_max": self.deterministic_eval.similarity_max,
            },
            "trace_summary": {
                "decision": "approve" if self.deterministic_eval.passed else "refine",
                "drift_score": float(self.deterministic_eval.drift_score),
                "diff_ratio": float(self.diff_ratio),
                "deterministic_pass": bool(self.deterministic_eval.passed),
            },
        }


@dataclass(frozen=True)
class YAMLMappingTransit:
    source_path: Path
    raw_text: str
    yaml_text: "YAMLTextTransit"
    payload: YAMLMappingPayload

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.data


@dataclass(frozen=True)
class YAMLTextTransit:
    source_path: Path
    raw_text: str
    payload: YAMLTextPayload

    def to_text(self) -> str:
        return self.raw_text


@dataclass(frozen=True)
class JSONMappingTransit:
    source_path: Path
    raw_text: str
    json_text: "JSONTextTransit"
    payload: JSONMappingPayload

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.data


@dataclass(frozen=True)
class JSONTextTransit:
    source_path: Path
    payload: JSONTextPayload

    def to_text(self) -> str:
        return self.payload.text


def _utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> JSONMappingTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise KernelError(f"Missing JSON file: {path}") from exc
    try:
        json_text = JSONTextTransit(source_path=path, payload=JSONTextPayload.model_validate({"text": raw_text}))
    except ValidationError as exc:
        raise KernelError(f"Invalid JSON text payload: {path}: {exc}") from exc
    try:
        data = json.loads(json_text.to_text())
    except json.JSONDecodeError as exc:
        raise KernelError(f"Invalid JSON: {path}: {exc}") from exc
    try:
        payload = JSONMappingPayload.model_validate({"data": data})
    except ValidationError as exc:
        raise KernelError(f"Invalid JSON mapping payload: {path}: {exc}") from exc
    return JSONMappingTransit(source_path=path, raw_text=json_text.to_text(), json_text=json_text, payload=payload)


def _load_ledger(path: Path) -> LedgerTransit:
    json_mapping = _load_json(path)
    raw = json_mapping.to_mapping()
    try:
        payload = LedgerPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid ledger payload: {exc}") from exc
    return LedgerTransit(json_mapping=json_mapping, raw=raw, payload=payload)


def _save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_yaml(path: Path) -> YAMLMappingTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise KernelError(f"Missing YAML file: {path}") from exc
    try:
        yaml_text_payload = YAMLTextPayload.model_validate({"text": raw_text})
    except ValidationError as exc:
        raise KernelError(f"Invalid YAML text payload: {path}: {exc}") from exc
    yaml_text = YAMLTextTransit(source_path=path, raw_text=yaml_text_payload.text, payload=yaml_text_payload)
    try:
        data = yaml.safe_load(yaml_text.to_text())
    except yaml.YAMLError as exc:
        raise KernelError(f"Invalid YAML: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise KernelError(f"Expected YAML mapping at {path}")
    try:
        payload = YAMLMappingPayload.model_validate({"data": data})
    except ValidationError as exc:
        raise KernelError(f"Invalid YAML mapping payload: {path}: {exc}") from exc
    return YAMLMappingTransit(source_path=path, raw_text=yaml_text.to_text(), yaml_text=yaml_text, payload=payload)


def _load_eval_config(path: Path) -> DeterministicEvalConfigTransit:
    yaml_mapping = _load_yaml(path)
    raw = yaml_mapping.to_mapping()
    try:
        payload = DeterministicEvalConfigPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid eval config payload: {path}: {exc}") from exc
    return DeterministicEvalConfigTransit(source_path=path, yaml_mapping=yaml_mapping, payload=payload)


def _load_metrics(path: Path) -> MetricsTransit:
    json_mapping = _load_json(path)
    raw = json_mapping.to_mapping()
    try:
        payload = MetricsPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid metrics payload: {path}: {exc}") from exc
    return MetricsTransit(json_mapping=json_mapping, raw=raw, payload=payload)


def _load_version_map(path: Path) -> VersionMapTransit:
    json_mapping = _load_json(path)
    raw = json_mapping.to_mapping()
    try:
        payload = VersionMapPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid version_map payload: {path}: {exc}") from exc
    return VersionMapTransit(json_mapping=json_mapping, raw=raw, payload=payload)


def _run_git(args: list[str]) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise KernelError(f"git {' '.join(args)} failed:\n{proc.stdout}")
    return proc.stdout


def _ensure_immutable_governance_files_unchanged() -> None:
    changed = _run_git(["diff", "--name-only"]).splitlines()
    blocked = sorted(set(changed) & IMMUTABLE_GOVERNANCE_FILES)
    if blocked:
        raise KernelError(
            "Immutable governance files modified; kernel refuses to proceed: " + ", ".join(blocked)
        )


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise KernelError(f"Missing file: {path}") from exc


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _read_prompt(path: Path) -> str:
    # Prompts are authored as markdown files; keep as-is after payload validation.
    return _load_prompt_text(path).to_prompt()


def _load_prompt_text(path: Path) -> PromptTextTransit:
    try:
        payload = PromptTextPayload.model_validate({"text": _read_text(path)})
    except ValidationError as exc:
        raise KernelError(f"Invalid prompt text payload: {path}: {exc}") from exc
    return PromptTextTransit(source_path=path, raw_text=payload.text, payload=payload)


def _load_roadmap_text(path: Path) -> RoadmapTextTransit:
    roadmap_text = _read_text(path)
    try:
        payload = RoadmapTextPayload.model_validate({"text": roadmap_text})
    except ValidationError as exc:
        raise KernelError(f"Invalid roadmap text payload: {path}: {exc}") from exc
    return RoadmapTextTransit(source_path=path, raw_text=roadmap_text, payload=payload)


def _load_chapter_text(path: Path) -> ChapterTextTransit:
    chapter_text = _read_text(path)
    try:
        payload = ChapterTextPayload.model_validate({"text": chapter_text})
    except ValidationError as exc:
        raise KernelError(f"Invalid chapter text payload: {path}: {exc}") from exc
    return ChapterTextTransit(source_path=path, raw_text=chapter_text, payload=payload)


def _load_writer_output(path: Path) -> WriterOutputTransit:
    writer_text = _read_text(path)
    try:
        payload = WriterOutputPayload.model_validate({"text": writer_text})
    except ValidationError as exc:
        raise KernelError(f"Invalid writer output payload: {path}: {exc}") from exc
    return WriterOutputTransit(source_path=path, raw_text=writer_text, payload=payload)


def _load_critic_eval_inputs() -> CriticEvalInputsTransit:
    chapter_quality = _load_yaml_text(EVAL_CHAPTER_QUALITY_PATH)
    style_guard = _load_yaml_text(EVAL_STYLE_GUARD_PATH)
    drift_detection = _load_yaml_text(EVAL_DRIFT_DETECTION_PATH)
    try:
        payload = CriticEvalInputsPayload.model_validate(
            {
                "chapter_quality": chapter_quality.to_text(),
                "style_guard": style_guard.to_text(),
                "drift_detection": drift_detection.to_text(),
            }
        )
    except ValidationError as exc:
        raise KernelError(f"Invalid critic eval inputs payload: {exc}") from exc
    return CriticEvalInputsTransit(
        payload=payload,
        chapter_quality=chapter_quality,
        style_guard=style_guard,
        drift_detection=drift_detection,
    )


def _load_yaml_text(path: Path) -> YAMLTextTransit:
    try:
        payload = YAMLTextPayload.model_validate({"text": _read_text(path)})
    except ValidationError as exc:
        raise KernelError(f"Invalid YAML text payload: {path}: {exc}") from exc
    return YAMLTextTransit(source_path=path, raw_text=payload.text, payload=payload)


def _strip_wrapping_code_fence(text: str) -> str:
    t = text.strip()
    if not t.startswith("```"):
        return t
    # Accept ```json / ```markdown, etc.
    first_nl = t.find("\n")
    if first_nl == -1:
        return t
    if not t.endswith("```"):
        return t
    inner = t[first_nl + 1 : -3]
    return inner.strip("\n")


def _extract_json_object(text: str) -> JSONMappingTransit:
    """Best-effort parse of a JSON object from an LLM response."""

    try:
        text_payload = LLMJSONResponseTextPayload.model_validate({"text": text})
    except ValidationError as exc:
        raise KernelError(f"Invalid LLM JSON response text payload: {exc}") from exc
    text_transit = LLMJSONResponseTextTransit(payload=text_payload)
    try:
        normalized_payload = LLMNormalizedJSONTextPayload.model_validate(
            {"text": _strip_wrapping_code_fence(text_transit.to_text()).strip()}
        )
    except ValidationError as exc:
        raise KernelError(f"Invalid normalized LLM JSON response text payload: {exc}") from exc
    normalized_transit = LLMNormalizedJSONTextTransit(response_text=text_transit, payload=normalized_payload)
    normalized_text = normalized_transit.to_text()
    lo = 0
    hi = len(normalized_text)
    candidate = normalized_text
    try:
        json.loads(candidate)
    except json.JSONDecodeError:
        # Try to locate the first {...} block.
        lo = normalized_text.find("{")
        hi = normalized_text.rfind("}") + 1
        if lo == -1 or hi <= lo:
            raise KernelError("LLM response did not contain a JSON object")
        candidate = normalized_text[lo:hi]
    try:
        object_text_payload = LLMJSONObjectTextPayload.model_validate(
            {"text": candidate, "start_index": lo, "end_index": hi}
        )
    except ValidationError as exc:
        raise KernelError(f"Invalid LLM response JSON object text payload: {exc}") from exc
    object_text = LLMJSONObjectTextTransit(response_text=text_transit, payload=object_text_payload)
    try:
        object_mapping_payload = LLMJSONObjectMappingPayload.model_validate_json(object_text.to_text())
    except ValidationError as exc:
        raise KernelError(f"LLM response contained invalid JSON object mapping: {exc}") from exc
    object_mapping = LLMJSONObjectMappingTransit(object_text=object_text, payload=object_mapping_payload)

    try:
        json_text = JSONTextTransit(
            source_path=Path("<llm-response>"),
            payload=JSONTextPayload.model_validate({"text": object_text.to_text()}),
        )
    except ValidationError as exc:
        raise KernelError(f"Invalid LLM response JSON text payload: {exc}") from exc
    try:
        payload = JSONMappingPayload.model_validate({"data": object_mapping.to_mapping()})
    except ValidationError as exc:
        raise KernelError(f"LLM response JSON must be an object mapping: {exc}") from exc
    return JSONMappingTransit(
        source_path=Path("<llm-response>"),
        raw_text=json_text.to_text(),
        json_text=json_text,
        payload=payload,
    )


def _extract_markdown(text: str) -> WriterOutputTransit:
    # Some models wrap markdown in ``` fences; unwrap if present.
    markdown = _strip_wrapping_code_fence(text).rstrip() + "\n"
    try:
        payload = WriterOutputPayload.model_validate({"text": markdown})
    except ValidationError as exc:
        raise KernelError(f"Invalid writer markdown payload from LLM response: {exc}") from exc
    return WriterOutputTransit(source_path=Path("<llm-response-markdown>"), raw_text=markdown, payload=payload)


def _llm_trace_dir(itdir: Path) -> Path:
    return itdir / "out" / "_llm_trace"


def _llm_write_trace(itdir: Path, *, name: str, prompt: str, response: str) -> None:
    tdir = _llm_trace_dir(itdir)
    tdir.mkdir(parents=True, exist_ok=True)
    _write_text(tdir / f"{name}.prompt.txt", prompt)
    _write_text(tdir / f"{name}.response.txt", response)


def _kernel_trace_path(itdir: Path) -> Path:
    return itdir / "out" / "kernel_trace.jsonl"


def _append_kernel_trace(itdir: Path, *, event: str, payload: dict[str, Any]) -> None:
    trace_path = _kernel_trace_path(itdir)
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": _utc_now_iso(), "event": event, "payload": payload}
    with trace_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, sort_keys=True) + "\n")


def _append_phase_trace(
    itdir: Path,
    *,
    phase: str,
    status: str,
    started_at_s: float,
    budget_signal: dict[str, Any],
) -> None:
    _append_kernel_trace(
        itdir,
        event="phase_trace",
        payload={
            "phase": phase,
            "status": status,
            "duration_ms": int(max(0.0, (_time.perf_counter() - started_at_s) * 1000)),
            "budget_signal": budget_signal,
        },
    )


def _llm_add_usage(a: Any, b: Any) -> Any:
    if a is None:
        return b
    if b is None:
        return a
    try:
        return type(a)(
            prompt_tokens=int(getattr(a, "prompt_tokens", 0) or 0) + int(getattr(b, "prompt_tokens", 0) or 0),
            completion_tokens=int(getattr(a, "completion_tokens", 0) or 0) + int(getattr(b, "completion_tokens", 0) or 0),
        )
    except Exception:
        return a


def _maybe_init_llm(cfg: LLMConfig) -> LLMRun | None:
    if not cfg.enabled:
        return None
    if LLMClient is None:
        raise KernelError("LLM mode requested but LLMClient is unavailable")
    try:
        client = LLMClient(
            provider=cfg.provider,
            model=cfg.model,
            base_url=cfg.base_url,
            api_key_env=cfg.api_key_env,
            timeout_s=cfg.timeout_s,
        )
    except Exception as exc:
        raise KernelError(f"Failed to initialize LLM client: {exc}") from exc
    usage = LLMUsage(prompt_tokens=0, completion_tokens=0)
    return LLMRun(client=client, usage=usage)


def _llm_generate_planner(itdir: Path, llm: LLMRun) -> Any:
    contract = _read_prompt(REPO_ROOT / "prompts" / "planner.md")
    planner_input_raw = _load_json(itdir / "in" / "planner_input.json").to_mapping()
    try:
        planner_input_payload = PlannerInputPayload.model_validate(planner_input_raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid planner input payload: {exc}") from exc
    planner_input = PlannerInputTransit.from_payload(planner_input_payload)
    user = "Return JSON only. No code fences. No commentary.\n\n" + "Planner input (JSON):\n" + planner_input.to_prompt_json()
    messages = [{"role": "system", "content": contract}, {"role": "user", "content": user}]
    try:
        resp = llm.client.chat(messages=messages, temperature=0.0)
    except LLMClientError as exc:
        raise KernelError(f"Planner LLM call failed: {exc}") from exc

    _llm_write_trace(itdir, name="planner", prompt=f"SYSTEM\n{contract}\n\nUSER\n{user}\n", response=resp.content)
    obj = _extract_json_object(resp.content).to_mapping()
    _write_text(itdir / "out" / "planner.json", json.dumps(obj, indent=2, sort_keys=True) + "\n")
    llm.usage = _llm_add_usage(llm.usage, resp.usage)
    return obj


def _llm_generate_writer(itdir: Path, llm: LLMRun, *, chapter_text: str, planner_json: str) -> str:
    contract = _read_prompt(REPO_ROOT / "prompts" / "writer.md")
    user = (
        "Output the full revised chapter markdown only. No code fences.\n\n"
        + "===CHAPTER_START===\n"
        + chapter_text.rstrip()
        + "\n===CHAPTER_END===\n\n"
        + "===PLANNER_JSON_START===\n"
        + planner_json.strip()
        + "\n===PLANNER_JSON_END===\n"
    )
    messages = [{"role": "system", "content": contract}, {"role": "user", "content": user}]
    try:
        resp = llm.client.chat(messages=messages, temperature=0.0)
    except LLMClientError as exc:
        raise KernelError(f"Writer LLM call failed: {exc}") from exc

    _llm_write_trace(itdir, name="writer", prompt=f"SYSTEM\n{contract}\n\nUSER\n{user}\n", response=resp.content)
    writer_output = _extract_markdown(resp.content)
    md = writer_output.to_markdown()
    _write_text(itdir / "out" / "writer.md", md)
    llm.usage = _llm_add_usage(llm.usage, resp.usage)
    return md


def _llm_generate_critic(itdir: Path, llm: LLMRun, *, revised_md: str) -> Any:
    contract = _read_prompt(REPO_ROOT / "prompts" / "critic.md")
    critic_eval_inputs = _load_critic_eval_inputs()
    user = (
        "Return JSON only. No code fences. No commentary.\n\n"
        + "evals/chapter-quality.yaml:\n"
        + critic_eval_inputs.chapter_quality.to_text()
        + "\n\n"
        + "evals/style-guard.yaml:\n"
        + critic_eval_inputs.style_guard.to_text()
        + "\n\n"
        + "evals/drift-detection.yaml:\n"
        + critic_eval_inputs.drift_detection.to_text()
        + "\n\n"
        + "Revised chapter markdown:\n"
        + revised_md
    )
    messages = [{"role": "system", "content": contract}, {"role": "user", "content": user}]
    try:
        resp = llm.client.chat(messages=messages, temperature=0.0)
    except LLMClientError as exc:
        raise KernelError(f"Critic LLM call failed: {exc}") from exc

    _llm_write_trace(itdir, name="critic", prompt=f"SYSTEM\n{contract}\n\nUSER\n{user}\n", response=resp.content)
    obj = _extract_json_object(resp.content).to_mapping()
    _write_text(itdir / "out" / "critic.json", json.dumps(obj, indent=2, sort_keys=True) + "\n")
    llm.usage = _llm_add_usage(llm.usage, resp.usage)
    return obj


def _markdown_headings(text: str) -> list[str]:
    return [line.rstrip("\n") for line in text.splitlines() if line.startswith("#")]


def _split_h2_sections(text: str) -> dict[str, str]:
    """Return a mapping of `## Heading` -> section body (excluding the heading line)."""

    lines = text.splitlines(keepends=True)
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        if line.startswith("## "):
            current = line.strip("\n")
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {k: "".join(v).strip() for k, v in sections.items()}


def _diff_size_ratio(old: str, new: str) -> float:
    """Approximate diff-size ratio as changed lines / original lines."""

    old_lines = old.splitlines()
    new_lines = new.splitlines()

    # Deterministic line-based comparison.
    # Count deletions + insertions as changed.
    import difflib

    sm = difflib.SequenceMatcher(a=old_lines, b=new_lines)
    changed = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        changed += (i2 - i1) + (j2 - j1)
    denom = max(1, len(old_lines))
    return min(1.0, changed / denom)


def _extract_roadmap_hypothesis(roadmap_md: str, chapter_id: str) -> str:
    """Best-effort extract of the chapter research hypothesis block from ROADMAP.md."""

    # ROADMAP uses headings like: "## Chapter 01 — Paradigm Shift"
    # Ledger chapter_id uses: "01-paradigm-shift".
    # We'll match on chapter number prefix.
    match = re.match(r"^(\d{2})-", chapter_id)
    if not match:
        return ""
    num = match.group(1)
    start_pat = re.compile(rf"^##\s+Chapter\s+{re.escape(num)}\b", re.MULTILINE)
    m = start_pat.search(roadmap_md)
    if not m:
        return ""
    start = m.start()
    # Next chapter or EOF
    next_m = re.search(r"^##\s+Chapter\s+\d{2}\b", roadmap_md[m.end() :], flags=re.MULTILINE)
    end = (m.end() + next_m.start()) if next_m else len(roadmap_md)
    block = roadmap_md[start:end]

    hypo_m = re.search(r"^###\s+Research hypothesis\s*$", block, flags=re.MULTILINE)
    if not hypo_m:
        return ""
    after = block[hypo_m.end() :]
    # Hypothesis is typically the next paragraph until the next ###
    stop = re.search(r"^###\s+", after, flags=re.MULTILINE)
    hypo = after[: stop.start()] if stop else after
    return hypo.strip()


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _cosine_sim(a: Counter[str], b: Counter[str]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(k, 0) for k, v in a.items())
    import math

    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return float(dot / (na * nb))


def _sentence_split(text: str) -> list[str]:
    # Deterministic, simple segmentation.
    parts = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text.strip()))
    return [p.strip() for p in parts if p.strip()]


def _duplicate_sentence_ratio(text: str) -> float:
    sents = [s.lower() for s in _sentence_split(text) if len(s) >= 20]
    if not sents:
        return 0.0
    total = len(sents)
    unique = len(set(sents))
    return float((total - unique) / total)


def _ngram_ratio(text: str, n: int = 5) -> float:
    toks = _tokenize(text)
    if len(toks) < n:
        return 0.0
    grams = [tuple(toks[i : i + n]) for i in range(0, len(toks) - n + 1)]
    total = len(grams)
    unique = len(set(grams))
    return float((total - unique) / total)


def _approx_adjective_density(text: str) -> float:
    """A deterministic heuristic (not POS-tagging).

    Approximates adjectives by common suffixes. This is intentionally conservative and stable.
    """

    toks = _tokenize(text)
    if not toks:
        return 0.0
    suffixes = ("ive", "ous", "ful", "less", "ic", "ical", "al", "ary", "y")
    hits = sum(1 for t in toks if len(t) >= 4 and t.endswith(suffixes))
    return float(hits / len(toks))


def _anchor_neighbors(text: str, term: str, window: int = 6) -> set[str]:
    toks = _tokenize(text)
    neighbors: set[str] = set()
    for i, tok in enumerate(toks):
        if tok != term:
            continue
        lo = max(0, i - window)
        hi = min(len(toks), i + window + 1)
        neighbors.update(toks[lo:hi])
    neighbors.discard(term)
    return neighbors


@dataclass(frozen=True)
class PlannerPlan:
    focus_areas: list[str]
    structural_changes: list[str]
    risk_flags: list[str]
    target_word_delta: str


@dataclass(frozen=True)
class CriticReport:
    structure_score: float
    clarity_score: float
    example_density: float
    tradeoff_presence: bool
    failure_modes_present: bool
    drift_score: float
    violations: list[str]
    decision: Literal["approve", "refine"]


@dataclass(frozen=True)
class PlannerPlanTransit:
    raw: dict[str, Any]
    payload: PlannerPlanPayload
    plan: PlannerPlan


@dataclass(frozen=True)
class CriticReportTransit:
    raw: dict[str, Any]
    payload: CriticReportPayload
    report: CriticReport


def _require_exact_keys(obj: dict[str, Any], keys: set[str], ctx: str) -> None:
    extra = set(obj.keys()) - keys
    missing = keys - set(obj.keys())
    if missing:
        raise KernelError(f"{ctx}: missing keys: {sorted(missing)}")
    if extra:
        raise KernelError(f"{ctx}: extra keys not allowed: {sorted(extra)}")


def _load_planner_plan(path: Path) -> PlannerPlanTransit:
    raw = _load_json(path).to_mapping()
    try:
        payload = PlannerPlanPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid planner output payload: {exc}") from exc
    plan = PlannerPlan(
        focus_areas=list(payload.focus_areas),
        structural_changes=list(payload.structural_changes),
        risk_flags=list(payload.risk_flags),
        target_word_delta=payload.target_word_delta,
    )
    return PlannerPlanTransit(raw=raw, payload=payload, plan=plan)


def _load_critic_report(path: Path) -> CriticReportTransit:
    raw = _load_json(path).to_mapping()
    try:
        payload = CriticReportPayload.model_validate(raw)
    except ValidationError as exc:
        raise KernelError(f"Invalid critic output payload: {exc}") from exc
    report = CriticReport(
        structure_score=payload.structure_score,
        clarity_score=payload.clarity_score,
        example_density=payload.example_density,
        tradeoff_presence=payload.tradeoff_presence,
        failure_modes_present=payload.failure_modes_present,
        drift_score=payload.drift_score,
        violations=list(payload.violations),
        decision=payload.decision,
    )
    return CriticReportTransit(raw=raw, payload=payload, report=report)


@dataclass(frozen=True)
class DeterministicEval:
    passed: bool
    chapter_quality: dict[str, Any]
    style_guard: dict[str, Any]
    drift_detection: dict[str, Any]
    drift_score: float
    similarity_max: float


def _eval_chapter_quality(text: str, cfg: ChapterQualityEvalConfigPayload) -> dict[str, Any]:
    required_sections = [
        "## Thesis",
        "## Why This Matters",
        "## System Breakdown",
        "## Concrete Example 1",
        "## Concrete Example 2",
        "## Trade-offs",
        "## Failure Modes",
        "## Research Directions",
    ]

    required_missing = [h for h in required_sections if h not in text]

    sections = _split_h2_sections(text)
    def nontrivial(heading: str, min_chars: int) -> bool:
        body = sections.get(heading, "")
        return len(body.strip()) >= min_chars

    scores: dict[str, float] = {
        "thesis_clarity": 1.0 if nontrivial("## Thesis", 120) else 0.0,
        "system_breakdown": 1.0 if nontrivial("## System Breakdown", 120) else 0.0,
        "examples_count": 1.0 if (nontrivial("## Concrete Example 1", 120) and nontrivial("## Concrete Example 2", 120)) else 0.0,
        "tradeoffs": 1.0 if nontrivial("## Trade-offs", 120) else 0.0,
        "failure_modes": 1.0 if nontrivial("## Failure Modes", 120) else 0.0,
    }

    # Forbidden hits (minimal, deterministic)
    forbidden_hits: list[str] = []
    forbidden_marketing = ["best-in-class", "world-class", "revolutionary", "effortless"]
    forbidden_anthro = ["the model thinks", "the agent wants", "the system feels"]
    forbidden_vague = ["obviously", "clearly", "just trust", "everyone knows"]
    lower = text.lower()
    for kw in forbidden_marketing:
        if kw in lower:
            forbidden_hits.append(f"marketing_language:{kw}")
    for kw in forbidden_anthro:
        if kw in lower:
            forbidden_hits.append(f"anthropomorphism:{kw}")
    for kw in forbidden_vague:
        if kw in lower:
            forbidden_hits.append(f"vague_claims:{kw}")

    total = sum(scores.values()) / max(1, len(scores))
    refine_min = float(cfg.thresholds.refine_min_total)

    passed = (not required_missing) and (not forbidden_hits) and (total >= refine_min)

    return {
        "pass": bool(passed),
        "required_missing": required_missing,
        "forbidden_hits": forbidden_hits,
        "scores": scores,
        "total": total,
        "timestamp": _utc_now_iso(),
    }


def _eval_style_guard(text: str, cfg: StyleGuardEvalConfigPayload) -> dict[str, Any]:
    max_words = int(cfg.limits.sentence_length.max_words)
    hard_fail_over = int(cfg.limits.sentence_length.hard_fail_over)
    max_adj_ratio = float(cfg.limits.adjective_density.max_ratio)

    sentences = _sentence_split(text)
    violations: list[dict[str, Any]] = []
    for s in sentences:
        words = re.findall(r"\b\w+\b", s)
        if len(words) > max_words:
            violations.append({"sentence": s[:200], "words": len(words)})

    adjective_density = _approx_adjective_density(text)

    forbidden_hits: list[str] = []
    for bucket, info in cfg.forbidden.items():
        for ex in info.examples:
            if ex.lower() in text.lower():
                forbidden_hits.append(f"{bucket}:{ex}")

    # Pass/fail: hard-fail if any sentence exceeds hard_fail_over or forbidden hits.
    hard_fail = any(v["words"] > hard_fail_over for v in violations)
    passed = (not hard_fail) and (adjective_density <= max_adj_ratio) and (not forbidden_hits)

    return {
        "pass": bool(passed),
        "sentence_length_violations": violations,
        "adjective_density": adjective_density,
        "forbidden_hits": forbidden_hits,
        "timestamp": _utc_now_iso(),
    }


def _eval_drift_detection(
    text: str,
    cfg: dict[str, Any],
    *,
    baseline_text: str | None,
    other_chapters: dict[str, str],
) -> tuple[dict[str, Any], float, float]:
    rules = cfg.get("rules", {}) if isinstance(cfg.get("rules"), dict) else {}

    hype_hits: list[str] = []
    hype = rules.get("stylistic_hype", {}) if isinstance(rules.get("stylistic_hype"), dict) else {}
    keywords = hype.get("keywords", []) if isinstance(hype.get("keywords"), list) else []
    patterns = hype.get("patterns", []) if isinstance(hype.get("patterns"), list) else []
    lower = text.lower()
    for kw in keywords:
        if isinstance(kw, str) and kw.lower() in lower:
            hype_hits.append(kw)
    for pat in patterns:
        if isinstance(pat, str) and re.search(pat, text):
            hype_hits.append(pat)

    repetition_metrics = {
        "duplicate_sentence_ratio": _duplicate_sentence_ratio(text),
        "near_duplicate_ngram_ratio": _ngram_ratio(text, n=5),
    }

    conceptual = rules.get("conceptual_drift", {}) if isinstance(rules.get("conceptual_drift"), dict) else {}
    anchors = conceptual.get("anchors", []) if isinstance(conceptual.get("anchors"), list) else []

    drift_metrics: dict[str, Any] = {"anchor_deltas": {}}
    max_delta = 0.0
    for a in anchors:
        if not isinstance(a, dict):
            continue
        term = a.get("term")
        if not isinstance(term, str) or not term:
            continue
        base_neighbors = _anchor_neighbors(baseline_text or "", term) if baseline_text else set()
        now_neighbors = _anchor_neighbors(text, term)
        if not base_neighbors and not now_neighbors:
            delta = 0.0
        else:
            jacc = 1.0 - (len(base_neighbors & now_neighbors) / max(1, len(base_neighbors | now_neighbors)))
            delta = float(jacc)
        drift_metrics["anchor_deltas"][term] = delta
        max_delta = max(max_delta, delta)

    # Cross-chapter similarity (bag-of-words cosine)
    this_vec = Counter(_tokenize(text))
    similarity_max = 0.0
    similarity_hits: list[dict[str, Any]] = []
    for other_id, other_text in other_chapters.items():
        sim = _cosine_sim(this_vec, Counter(_tokenize(other_text)))
        similarity_max = max(similarity_max, sim)
        if sim >= 0.85:
            similarity_hits.append({"chapter_id": other_id, "cosine": sim})

    drift_metrics["cross_chapter_similarity_hits"] = similarity_hits

    # Drift score: aggregate of hype + repetition + conceptual drift.
    dup_ratio = float(repetition_metrics["duplicate_sentence_ratio"])
    ng_ratio = float(repetition_metrics["near_duplicate_ngram_ratio"])
    hype_flag = 1.0 if hype_hits else 0.0

    # Normalize repetition against YAML tolerances when present.
    rep_cfg = rules.get("repetition", {}) if isinstance(rules.get("repetition"), dict) else {}
    max_dup = float(rep_cfg.get("max_duplicate_sentence_ratio", 0.08))
    max_ng = float(rep_cfg.get("max_near_duplicate_ngram_ratio", 0.12))
    rep_component = 0.5 * min(1.0, dup_ratio / max(1e-9, max_dup)) + 0.5 * min(1.0, ng_ratio / max(1e-9, max_ng))

    concept_cfg = rules.get("conceptual_drift", {}) if isinstance(rules.get("conceptual_drift"), dict) else {}
    max_neighbor_delta = float(concept_cfg.get("max_neighbor_jaccard_delta", 0.35))
    concept_component = min(1.0, max_delta / max(1e-9, max_neighbor_delta))

    sim_component = 1.0 if similarity_hits else 0.0
    drift_score = min(1.0, 0.25 * hype_flag + 0.35 * rep_component + 0.30 * concept_component + 0.10 * sim_component)

    report = {
        "pass": bool(drift_score <= 0.30 and not hype_hits),
        "hype_hits": hype_hits,
        "repetition_metrics": repetition_metrics,
        "drift_metrics": drift_metrics,
        "timestamp": _utc_now_iso(),
    }
    return report, float(drift_score), float(similarity_max)


def run_deterministic_evals(
    chapter_text: str,
    *,
    baseline_text: str | None,
    other_chapters: OtherChaptersTransit,
) -> DeterministicEval:
    transit = DeterministicEvalTransit(
        chapter_quality=_load_eval_config(EVAL_CHAPTER_QUALITY_PATH),
        style_guard=_load_eval_config(EVAL_STYLE_GUARD_PATH),
        drift_detection=_load_eval_config(EVAL_DRIFT_DETECTION_PATH),
    )
    try:
        rules_transit = DeterministicEvalRulesTransit(
            chapter_quality=ChapterQualityEvalConfigPayload.model_validate(transit.chapter_quality.payload.model_dump()),
            style_guard=StyleGuardEvalConfigPayload.model_validate(transit.style_guard.payload.model_dump()),
        )
    except ValidationError as exc:
        raise KernelError(f"Invalid deterministic eval rules payload: {exc}") from exc
    d_cfg = transit.drift_detection.payload.model_dump()

    chapter_quality = _eval_chapter_quality(chapter_text, rules_transit.chapter_quality)
    style_guard = _eval_style_guard(chapter_text, rules_transit.style_guard)
    drift_detection, drift_score, similarity_max = _eval_drift_detection(
        chapter_text,
        d_cfg,
        baseline_text=baseline_text,
        other_chapters=other_chapters.as_mapping(),
    )

    passed = bool(chapter_quality.get("pass") and style_guard.get("pass") and drift_detection.get("pass"))
    return DeterministicEval(
        passed=passed,
        chapter_quality=chapter_quality,
        style_guard=style_guard,
        drift_detection=drift_detection,
        drift_score=float(drift_score),
        similarity_max=float(similarity_max),
    )


def _declared_section_set(plan: PlannerPlan, headings: Iterable[str]) -> set[str]:
    available = {h for h in headings if h.startswith("## ")}
    declared: set[str] = set()
    hay = "\n".join(plan.focus_areas + plan.structural_changes + plan.risk_flags)
    for h in available:
        if h in hay:
            declared.add(h)
    return declared


def _changed_sections(old: str, new: str) -> set[str]:
    a = _split_h2_sections(old)
    b = _split_h2_sections(new)
    changed: set[str] = set()
    for h in set(a.keys()) | set(b.keys()):
        if a.get(h, "") != b.get(h, ""):
            changed.add(h)
    return changed


def _critic_score(report: CriticReport) -> float:
    return float((report.structure_score + report.clarity_score + report.example_density) / 3.0)


def _load_other_chapters_text(ledger: LedgerPayload, current_chapter_id: str) -> OtherChaptersTransit:
    entries: list[OtherChapterTextTransit] = []
    for cid, meta in ledger.chapters.items():
        if cid == current_chapter_id:
            continue
        if not meta.path:
            continue
        try:
            chapter_text = _load_chapter_text(REPO_ROOT / meta.path)
        except KernelError:
            continue
        entries.append(OtherChapterTextTransit(chapter_id=cid, chapter_text=chapter_text))
    return OtherChaptersTransit(entries=tuple(entries))


def _kernel_iteration_dir(io_dir: Path, chapter_id: str, iteration: int) -> Path:
    return io_dir / chapter_id / f"iter_{iteration:02d}"


def _prepare_iteration_inputs(
    *,
    io_dir: Path,
    chapter_id: str,
    iteration: int,
    chapter_text: str,
    ledger_chapter: LedgerChapterPayload,
    previous_critic: dict[str, Any] | None,
) -> None:
    itdir = _kernel_iteration_dir(io_dir, chapter_id, iteration)
    (itdir / "in").mkdir(parents=True, exist_ok=True)
    (itdir / "out").mkdir(parents=True, exist_ok=True)

    roadmap_text = _load_roadmap_text(ROADMAP_PATH)
    hypothesis = _extract_roadmap_hypothesis(roadmap_text.to_text(), chapter_id)
    planner_input = PlannerInputTransit(
        chapter_id=chapter_id,
        chapter_content=chapter_text,
        quality_metrics=ledger_chapter.quality_metrics,
        previous_critic_feedback=previous_critic,
        chapter_hypothesis=hypothesis,
    )
    _write_text(
        itdir / "in" / "planner_input.json",
        json.dumps(dataclasses.asdict(planner_input), indent=2, sort_keys=True) + "\n",
    )

    # Writer input is chapter + planner output (planner output will be produced in out/planner.json).
    _write_text(itdir / "in" / "writer_chapter.md", chapter_text)
    _write_text(
        itdir / "in" / "writer_instructions.txt",
        "Writer must use out/planner.json as the plan and write full revised chapter to out/writer.md\n",
    )

    _write_text(
        itdir / "in" / "critic_instructions.txt",
        "Critic must evaluate out/writer.md and write JSON report to out/critic.json\n",
    )


def run_kernel(
    *,
    chapter_id: str,
    io_dir: Path,
    max_iterations: int,
    max_diff_ratio: float,
    max_drift_score: float,
    require_two_consecutive_passes: bool,
    commit_on_refine: bool,
    verbose: bool = False,
    llm_config: LLMConfig | None = None,
) -> int:
    _ensure_immutable_governance_files_unchanged()

    llm = _maybe_init_llm(
        llm_config
        if llm_config is not None
        else LLMConfig(
            enabled=False,
            provider="mock",
            model="",
            base_url=None,
            api_key_env="COPILOT_API_KEY",
            timeout_s=90,
        )
    )

    try:
        ledger_transit = _load_ledger(LEDGER_PATH)
        ledger = ledger_transit.raw
        ledger_payload = ledger_transit.payload
        chapter_meta_payload = ledger_payload.chapters.get(chapter_id)
        if chapter_meta_payload is None:
            raise KernelError(f"Unknown chapter_id: {chapter_id}")
        chapter_meta: dict[str, Any] = chapter_meta_payload.model_dump(exclude_none=True)
        chapters_obj = ledger.get("chapters")
        if not isinstance(chapters_obj, dict):
            raise KernelError("Invalid ledger: chapters must be an object")
        chapters_obj[chapter_id] = chapter_meta
        status = chapter_meta_payload.status
        lifecycle = chapter_meta_payload.lifecycle
        _vprint(
            verbose,
            f"kernel: chapter_id={chapter_id} status={status!r} lifecycle={lifecycle!r} max_iterations={max_iterations} max_diff_ratio={max_diff_ratio:.2f} max_drift_score={max_drift_score:.2f}",
        )
        if status in {"locked", "hold"}:
            if status == "hold":
                hint = f" Try: uv run python state/governance_engine.py unhold --chapter-id {chapter_id}"
            elif status == "locked":
                hint = f" Try: uv run python state/governance_engine.py unlock --chapter-id {chapter_id}"
            else:
                hint = ""
            raise KernelError(f"Chapter is not eligible (status={status!r})." + hint)
        if lifecycle == "frozen":
            raise KernelError("Chapter is frozen.")

        chapter_path = chapter_meta_payload.path
        if not chapter_path:
            raise KernelError("Chapter is missing a valid path")
        chapter_file = REPO_ROOT / chapter_path
        baseline_text = _load_chapter_text(chapter_file).to_text()
        _vprint(verbose, f"kernel: chapter_path={chapter_path}")

        previous_critic: dict[str, Any] | None = None
        # If ledger has last_eval and it is critic-like, pass through.
        if isinstance(chapter_meta_payload.last_eval, dict):
            previous_critic = chapter_meta_payload.last_eval

        other_chapters = _load_other_chapters_text(ledger_payload, chapter_id)
        original_headings = _markdown_headings(baseline_text)

        consecutive_passes = int(chapter_meta_payload.stability.get("consecutive_passes", 0) or 0)
        current_iteration = int(chapter_meta_payload.current_iteration or 0)

        for i in range(1, max_iterations + 1):
            iteration = current_iteration + i
            itdir = _kernel_iteration_dir(io_dir, chapter_id, iteration)
            _vprint(verbose, f"iter {iteration}: start (io={itdir.relative_to(REPO_ROOT)})")
            _append_kernel_trace(
                itdir,
                event="iteration_started",
                payload={
                    "chapter_id": chapter_id,
                    "iteration": iteration,
                    "max_diff_ratio": max_diff_ratio,
                    "max_drift_score": max_drift_score,
                },
            )
            try:
                ledger_chapter_for_iteration = LedgerChapterPayload.model_validate(chapter_meta)
            except ValidationError as exc:
                raise KernelError(f"Invalid chapter ledger payload: {exc}") from exc
            _prepare_iteration_inputs(
                io_dir=io_dir,
                chapter_id=chapter_id,
                iteration=iteration,
                chapter_text=_load_chapter_text(chapter_file).to_text(),
                ledger_chapter=ledger_chapter_for_iteration,
                previous_critic=previous_critic,
            )

            planner_out = itdir / "out" / "planner.json"
            writer_out = itdir / "out" / "writer.md"
            critic_out = itdir / "out" / "critic.json"
            role_phase_started_at = _time.perf_counter()

            llm_iter_usage = None
            if llm is not None:
                before_prompt = int(getattr(llm.usage, "prompt_tokens", 0) or 0)
                before_completion = int(getattr(llm.usage, "completion_tokens", 0) or 0)

                if verbose and (not planner_out.exists() or not writer_out.exists() or not critic_out.exists()):
                    missing = []
                    if not planner_out.exists():
                        missing.append("planner")
                    if not writer_out.exists():
                        missing.append("writer")
                    if not critic_out.exists():
                        missing.append("critic")
                    _vprint(verbose, f"iter {iteration}: llm generating missing outputs: {', '.join(missing)}")

                # Generate any missing role outputs in dependency order.
                if not planner_out.exists():
                    _llm_generate_planner(itdir, llm)

                planner_json_transit = _load_json(planner_out) if planner_out.exists() else None
                planner_json_text = planner_json_transit.raw_text if planner_json_transit is not None else ""

                if not writer_out.exists():
                    _llm_generate_writer(
                        itdir,
                        llm,
                        chapter_text=_load_chapter_text(chapter_file).to_text(),
                        planner_json=planner_json_text,
                    )

                revised_md = _load_writer_output(writer_out).to_markdown() if writer_out.exists() else ""

                if not critic_out.exists():
                    _llm_generate_critic(itdir, llm, revised_md=revised_md)

                after_prompt = int(getattr(llm.usage, "prompt_tokens", 0) or 0)
                after_completion = int(getattr(llm.usage, "completion_tokens", 0) or 0)
                llm_iter_usage = LLMUsage(
                    prompt_tokens=max(0, after_prompt - before_prompt),
                    completion_tokens=max(0, after_completion - before_completion),
                )

            if not planner_out.exists() or not writer_out.exists() or not critic_out.exists():
                _append_phase_trace(
                    itdir,
                    phase="role_output_ready",
                    status="failed",
                    started_at_s=role_phase_started_at,
                    budget_signal={
                        "missing_outputs": int(not planner_out.exists())
                        + int(not writer_out.exists())
                        + int(not critic_out.exists())
                    },
                )
                sys.stderr.write(
                    "Role outputs missing for this iteration. Produce these files and re-run:\n"
                    f"- {planner_out.relative_to(REPO_ROOT)}\n"
                    f"- {writer_out.relative_to(REPO_ROOT)}\n"
                    f"- {critic_out.relative_to(REPO_ROOT)}\n"
                )
                return 2
            _append_phase_trace(
                itdir,
                phase="role_output_ready",
                status="ok",
                started_at_s=role_phase_started_at,
                budget_signal={
                    "llm_prompt_tokens": int(getattr(llm_iter_usage, "prompt_tokens", 0) or 0),
                    "llm_completion_tokens": int(getattr(llm_iter_usage, "completion_tokens", 0) or 0),
                },
            )

            evaluation_phase_started_at = _time.perf_counter()
            plan_transit = _load_planner_plan(planner_out)
            plan = plan_transit.plan
            revised = _load_writer_output(writer_out).to_markdown()
            critic_transit = _load_critic_report(critic_out)
            critic = critic_transit.report

            revised_headings = _markdown_headings(revised)
            if revised_headings != original_headings:
                raise KernelError("Writer changed headings; this is forbidden.")

            current_chapter_text = _load_chapter_text(chapter_file).to_text()
            diff_ratio = _diff_size_ratio(current_chapter_text, revised)
            _vprint(verbose, f"iter {iteration}: diff_ratio={diff_ratio:.2f} (limit {max_diff_ratio:.2f})")
            if diff_ratio > max_diff_ratio:
                raise KernelError(f"Writer diff size too large ({diff_ratio:.2f} > {max_diff_ratio:.2f}).")

            declared = _declared_section_set(plan, original_headings)
            if not declared:
                raise KernelError("Planner did not explicitly reference any existing '##' headings.")
            changed = _changed_sections(current_chapter_text, revised)
            illegal = sorted(changed - declared)
            if illegal:
                raise KernelError("Writer modified undeclared sections: " + ", ".join(illegal))

            det = run_deterministic_evals(revised, baseline_text=baseline_text, other_chapters=other_chapters)
            if det.drift_score > max_drift_score:
                det_pass = False
            else:
                det_pass = det.passed

            pass_now = (critic.decision == "approve") and det_pass
            _vprint(
                verbose,
                f"iter {iteration}: critic_decision={critic.decision!r} det_pass={bool(det_pass)} drift_score={float(det.drift_score):.2f} pass_now={bool(pass_now)}",
            )
            _append_kernel_trace(
                itdir,
                event="iteration_evaluated",
                payload={
                    "iteration": iteration,
                    "critic_decision": critic.decision,
                    "diff_ratio": float(diff_ratio),
                    "drift_score": float(det.drift_score),
                    "deterministic_pass": bool(det_pass),
                    "pass_now": bool(pass_now),
                },
            )
            _append_phase_trace(
                itdir,
                phase="evaluation",
                status="pass" if pass_now else "refine",
                started_at_s=evaluation_phase_started_at,
                budget_signal={
                    "diff_ratio": float(diff_ratio),
                    "drift_score": float(det.drift_score),
                    "deterministic_pass": bool(det_pass),
                },
            )

            persistence_phase_started_at = _time.perf_counter()
            if pass_now:
                consecutive_passes += 1
            else:
                consecutive_passes = 0

            # Persist chapter content only after validations and eval run.
            _write_text(chapter_file, revised)

            # Update chapter state
            chapter_meta["current_iteration"] = iteration
            chapter_meta["revision_count"] = int(chapter_meta.get("revision_count", 0) or 0) + 1
            chapter_meta["last_eval"] = {
                "critic": dataclasses.asdict(critic),
                "deterministic": {
                    "passed": det.passed,
                    "drift_score": det.drift_score,
                    "similarity_max": det.similarity_max,
                    "chapter_quality": det.chapter_quality,
                    "style_guard": det.style_guard,
                    "drift_detection": det.drift_detection,
                },
            }
            chapter_meta["quality_metrics"] = {
                "structure_score": critic.structure_score,
                "clarity_score": critic.clarity_score,
                "example_density": critic.example_density,
                "tradeoff_presence": bool(critic.tradeoff_presence),
                "failure_mode_presence": bool(critic.failure_modes_present),
                "drift_score": float(det.drift_score),
            }
            chapter_meta.setdefault("stability", {})
            chapter_meta["stability"]["consecutive_passes"] = consecutive_passes
            chapter_meta["stability"]["last_modified_iteration"] = iteration

            chapter_meta.setdefault("iteration_log", [])
            chapter_meta["iteration_log"].append(
                {
                    "iteration": iteration,
                    "planner_focus": list(plan.focus_areas),
                    "critic_score": _critic_score(critic),
                    "drift_score": float(det.drift_score),
                    "diff_size": float(diff_ratio),
                }
            )

            # Update metrics.json (minimal, per schema)
            metrics_transit = _load_metrics(METRICS_PATH)
            metrics = metrics_transit.raw
            metrics.setdefault("chapters", {})
            ch_metrics = metrics["chapters"].setdefault(chapter_id, {})
            ch_metrics.setdefault("history", [])
            metrics_history = MetricsHistoryTransit(
                iteration=iteration,
                critic=critic,
                deterministic_eval=det,
                diff_ratio=diff_ratio,
            )
            ch_metrics["history"].append(metrics_history.to_metrics_entry())
            _save_json(METRICS_PATH, metrics)

            # Update repo_iteration_log (minimal entry)
            ledger.setdefault("repo_iteration_log", [])
            repo_log = ledger["repo_iteration_log"]
            if isinstance(repo_log, list):
                repo_iter = (max((int(e.get("iteration", 0) or 0) for e in repo_log if isinstance(e, dict)), default=0) + 1)
                repo_log.append(
                    {
                        "iteration": repo_iter,
                        "timestamp": _utc_now_iso(),
                        "agent_task": "kernel_refine",
                        "inputs": {
                            "changed_files": [chapter_path, "state/ledger.json", "state/metrics.json"],
                            "notes": f"Kernel refinement iteration {iteration} for {chapter_id}",
                        },
                        "scope": {
                            "chapters_modified": [chapter_id],
                            "patterns_modified": [],
                            "governance_modified": False,
                        },
                        "resource_usage": {
                            "prompt_tokens": int(getattr(llm_iter_usage, "prompt_tokens", 0) or 0) if llm_iter_usage is not None else 0,
                            "completion_tokens": int(getattr(llm_iter_usage, "completion_tokens", 0) or 0) if llm_iter_usage is not None else 0,
                            "eval_runtime_ms": 0,
                        },
                        "evals": {
                            "chapter_quality": det.chapter_quality,
                            "style_guard": det.style_guard,
                            "drift_detection": det.drift_detection,
                        },
                        "outcome": {
                            "status": "passed" if pass_now else "refine",
                            "decision": "approve" if pass_now else "refine",
                            "rationale": "Deterministic eval + critic decision gating.",
                        },
                        "artifacts": {
                            "commit_hash": None,
                            "diff_summary": f"diff_ratio={diff_ratio:.2f}; drift_score={det.drift_score:.2f}",
                        },
                    }
                )

            _save_json(LEDGER_PATH, ledger)
            _vprint(verbose, f"iter {iteration}: persisted state (consecutive_passes={consecutive_passes})")
            _append_kernel_trace(
                itdir,
                event="state_persisted",
                payload={
                    "iteration": iteration,
                    "consecutive_passes": int(consecutive_passes),
                    "status": chapter_meta.get("status"),
                    "lifecycle": chapter_meta.get("lifecycle"),
                },
            )
            _append_phase_trace(
                itdir,
                phase="state_persistence",
                status="ok",
                started_at_s=persistence_phase_started_at,
                budget_signal={
                    "consecutive_passes": int(consecutive_passes),
                    "require_two_consecutive_passes": bool(require_two_consecutive_passes),
                },
            )

            # Transition logic
            if pass_now:
                if (not require_two_consecutive_passes) or consecutive_passes >= 2:
                    chapter_meta["lifecycle"] = "refined"
                    _save_json(LEDGER_PATH, ledger)
                    _append_kernel_trace(
                        itdir,
                        event="lifecycle_transition",
                        payload={"iteration": iteration, "new_lifecycle": "refined"},
                    )

                    if commit_on_refine:
                        _run_git(["add", chapter_path, "state/ledger.json", "state/metrics.json"])
                        _run_git(["commit", "-m", f"refine: {chapter_id} (iter {iteration})"])
                        commit_hash = _run_git(["rev-parse", "HEAD"]).strip()
                        version_map_transit = _load_version_map(VERSION_MAP_PATH)
                        _save_json(VERSION_MAP_PATH, version_map_transit.with_commit(chapter_id, commit_hash))

                    return 0

            previous_critic = dataclasses.asdict(critic)

        # Max iterations reached
        _vprint(verbose, "kernel: max iterations reached; setting status='hold'")
        chapter_meta["status"] = "hold"
        _save_json(LEDGER_PATH, ledger)
        return 1
    finally:
        if llm is not None:
            client = getattr(llm, "client", None)
            if client is not None:
                close_fn = getattr(client, "close", None)
                if callable(close_fn):
                    try:
                        close_fn()
                    except Exception as exc:
                        sys.stderr.write(f"WARN: LLM client close failed: {exc}\n")
                else:
                    stop_fn = getattr(client, "stop", None)
                    if callable(stop_fn):
                        try:
                            stop_fn()
                        except Exception as exc:
                            sys.stderr.write(f"WARN: LLM client stop failed: {exc}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kernel", description="Deterministic Planner→Writer→Critic refinement kernel")
    parser.add_argument("--chapter-id")
    parser.add_argument(
        "--list-chapters",
        action="store_true",
        help="List available chapter IDs (from book/chapters/*.md) and exit.",
    )
    parser.add_argument("--io-dir", type=Path, default=REPO_ROOT / "state" / "role_io")
    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--max-diff-ratio", type=float, default=0.35)
    parser.add_argument("--max-drift-score", type=float, default=0.30)
    passes_group = parser.add_mutually_exclusive_group()
    passes_group.add_argument(
        "--require-two-consecutive-passes",
        action="store_true",
        default=None,
        help="Require 2 consecutive clean passes before promoting to refined (default).",
    )
    passes_group.add_argument(
        "--no-require-two-consecutive-passes",
        action="store_false",
        dest="require_two_consecutive_passes",
        default=None,
        help="Promote to refined after a single clean pass.",
    )
    parser.add_argument("--commit", action="store_true", help="Commit on promote-to-refined")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print iteration progress and gate metrics")

    parser.add_argument(
        "--llm",
        action="store_true",
        help="Auto-generate missing Planner/Writer/Critic outputs via an LLM (writes the same out/*.json/md files).",
    )
    parser.add_argument(
        "--llm-provider",
        default=os.environ.get("KERNEL_LLM_PROVIDER", "copilot"),
        help="LLM provider: copilot | mock (default: env KERNEL_LLM_PROVIDER or copilot)",
    )
    parser.add_argument(
        "--llm-model",
        default=os.environ.get("KERNEL_LLM_MODEL", ""),
        help="LLM model name (default: env KERNEL_LLM_MODEL). Required when --llm is set.",
    )
    parser.add_argument(
        "--llm-base-url",
        default=os.environ.get("KERNEL_LLM_BASE_URL", None),
        help="Override provider base URL (default: env KERNEL_LLM_BASE_URL).",
    )
    parser.add_argument(
        "--llm-api-key-env",
        default=os.environ.get("KERNEL_LLM_API_KEY_ENV", "COPILOT_API_KEY"),
        help="Env var name containing API key (only when Copilot SDK is configured for BYOK). Default: COPILOT_API_KEY.",
    )
    parser.add_argument(
        "--llm-timeout-s",
        type=int,
        default=int(os.environ.get("KERNEL_LLM_TIMEOUT_S", "90")),
        help="LLM HTTP timeout seconds (default: env KERNEL_LLM_TIMEOUT_S or 90).",
    )

    args = parser.parse_args(argv)
    try:
        cli_args = KernelCLIArgsTransit.from_namespace(args)
    except ValidationError as exc:
        raise KernelError(f"Invalid CLI args payload: {exc}") from exc

    if cli_args.payload.list_chapters:
        chapters_dir = REPO_ROOT / "book" / "chapters"
        chapter_paths = sorted(chapters_dir.glob("*.md"))
        for path in chapter_paths:
            sys.stdout.write(path.stem + "\n")
        return 0

    chapter_id = cli_args.payload.chapter_id
    if not chapter_id:
        raise KernelError("--chapter-id is required (or use --list-chapters)")
    require_two_consecutive_passes = (
        True
        if cli_args.payload.require_two_consecutive_passes is None
        else bool(cli_args.payload.require_two_consecutive_passes)
    )

    llm_cfg: LLMConfig | None = None
    if cli_args.payload.llm:
        provider = cli_args.payload.llm_provider
        allowed = {"copilot", "mock"}
        if provider not in allowed:
            raise KernelError(f"--llm-provider must be one of {sorted(allowed)}")
        model = cli_args.payload.llm_model.strip()
        if not model and provider != "mock":
            raise KernelError("--llm-model (or env KERNEL_LLM_MODEL) is required when --llm is set")

        llm_cfg = LLMConfig(
            enabled=True,
            provider=provider,  # type: ignore[arg-type]
            model=model or "mock",
            base_url=(cli_args.payload.llm_base_url if cli_args.payload.llm_base_url else None),
            api_key_env=cli_args.payload.llm_api_key_env,
            timeout_s=cli_args.payload.llm_timeout_s,
        )
    try:
        return int(
            run_kernel(
                chapter_id=chapter_id,
                io_dir=cli_args.payload.io_dir,
                max_iterations=cli_args.payload.max_iterations,
                max_diff_ratio=cli_args.payload.max_diff_ratio,
                max_drift_score=cli_args.payload.max_drift_score,
                require_two_consecutive_passes=require_two_consecutive_passes,
                commit_on_refine=cli_args.payload.commit,
                verbose=cli_args.payload.verbose,
                llm_config=llm_cfg,
            )
        )
    except KernelError as exc:
        sys.stderr.write(f"KernelError: {exc}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
