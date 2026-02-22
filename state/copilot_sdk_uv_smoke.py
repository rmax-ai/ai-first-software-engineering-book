#!/usr/bin/env python3
"""Copilot SDK smoke test using uv-managed dependencies.

Run:
  uv run python state/copilot_sdk_uv_smoke.py
  uv run python state/copilot_sdk_uv_smoke.py --mode prompt --model gpt-5
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass
import importlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_PATH = REPO_ROOT / "state" / "kernel.py"
METRICS_PATH = REPO_ROOT / "state" / "metrics.json"
TRACE_SUMMARY_FIXTURE_ROOT = REPO_ROOT / "state" / ".smoke_fixtures" / "trace_summary"
TRACE_SUMMARY_MODE_SPECS: dict[str, dict[str, bool]] = {
    "trace-summary": {},
    "trace-summary-malformed-phase": {
        "expect_phase_trace_failure": True,
        "inject_malformed_phase_trace": True,
    },
    "trace-summary-malformed-phase-payload": {
        "expect_phase_trace_failure": True,
        "inject_non_object_phase_payload": True,
    },
    "trace-summary-missing-phase": {
        "expect_phase_trace_failure": True,
        "inject_missing_required_phase_trace": True,
    },
}


class TraceSummaryPayload(BaseModel):
    decision: str
    drift_score: float
    diff_ratio: float
    deterministic_pass: bool


class MetricsHistoryEntryPayload(BaseModel):
    iteration: int
    trace_summary: TraceSummaryPayload


class MetricsChapterPayload(BaseModel):
    history: list[MetricsHistoryEntryPayload]


class MetricsPayload(BaseModel):
    chapters: dict[str, MetricsChapterPayload]


@dataclass(frozen=True)
class MetricsTransit:
    json_mapping: JSONMappingTransit
    raw: dict[str, Any]
    payload: MetricsPayload


class KernelTraceEntryPayload(BaseModel):
    event: str
    payload: Any


class KernelTracePayload(BaseModel):
    entries: list[KernelTraceEntryPayload]


class KernelTracePhaseEntryPayload(BaseModel):
    event: str
    payload: dict[str, Any]


class PhaseTracePayload(BaseModel):
    phase: str
    status: str
    duration_ms: int
    budget_signal: str


class KernelFixtureLedgerChapterPayload(BaseModel):
    path: str
    status: str | None = None
    lifecycle: str | None = None


class KernelFixtureChapterMappingPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    path: str
    status: str | None = None
    lifecycle: str | None = None


class KernelFixtureLedgerPayload(BaseModel):
    chapters: dict[str, KernelFixtureLedgerChapterPayload]


class JSONMappingPayload(BaseModel):
    data: dict[str, Any]


class JSONTextPayload(BaseModel):
    text: str


class JSONLinePayload(BaseModel):
    line_number: int
    data: dict[str, Any]


class JSONLineTextPayload(BaseModel):
    line_number: int
    text: str


class JSONLinesPayload(BaseModel):
    entries: list[JSONLinePayload]


class KernelTraceTextPayload(BaseModel):
    text: str


class SDKSessionEventDataPayload(BaseModel):
    content: str | None = None
    message: str | None = None


class SDKSessionEventPayload(BaseModel):
    type: str | None = None
    data: SDKSessionEventDataPayload | None = None


class SDKEventObjectPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    data: dict[str, Any]


class SmokeCLIArgsPayload(BaseModel):
    mode: Literal[
        "ping",
        "prompt",
        "trace-summary",
        "trace-summary-malformed-phase",
        "trace-summary-malformed-phase-payload",
        "trace-summary-missing-phase",
    ]
    model: str
    prompt: str
    timeout: float
    chapter_id: str
    kernel_max_iterations: int
    run_kernel_for_trace_summary: bool
    metrics_path: str
    trace_summary_fixture_root: str


@dataclass(frozen=True)
class KernelFixtureLedgerTransit:
    json_mapping: JSONMappingTransit
    raw: dict[str, Any]
    payload: KernelFixtureLedgerPayload


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


@dataclass(frozen=True)
class JSONLinesTransit:
    payload: JSONLinesPayload

    @classmethod
    def from_payload(cls, payload: JSONLinesPayload) -> "JSONLinesTransit":
        return cls(payload=payload)

    def to_mappings(self) -> list[dict[str, Any]]:
        return [entry.data for entry in self.payload.entries]


@dataclass(frozen=True)
class JSONLineTransit:
    payload: JSONLinePayload

    @classmethod
    def from_mapping(cls, line_number: int, parsed_line: dict[str, Any]) -> "JSONLineTransit":
        return cls(payload=JSONLinePayload.model_validate({"line_number": line_number, "data": parsed_line}))

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.model_dump()


@dataclass(frozen=True)
class JSONLineTextTransit:
    payload: JSONLineTextPayload

    @classmethod
    def from_line(cls, line_number: int, text: str) -> "JSONLineTextTransit":
        return cls(payload=JSONLineTextPayload.model_validate({"line_number": line_number, "text": text}))

    @property
    def line_number(self) -> int:
        return self.payload.line_number

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class KernelTraceTextTransit:
    source_path: Path
    payload: KernelTraceTextPayload

    def lines(self) -> list[str]:
        return self.payload.text.splitlines()


@dataclass(frozen=True)
class MetricsHistoryTransit:
    iteration: int
    trace_summary: TraceSummaryPayload


@dataclass(frozen=True)
class TraceSummaryTransit:
    payload: TraceSummaryPayload

    @classmethod
    def from_payload(cls, payload: TraceSummaryPayload) -> "TraceSummaryTransit":
        return cls(payload=payload)

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.model_dump()


@dataclass(frozen=True)
class PhaseTraceTransit:
    phase: str
    status: str
    duration_ms: int
    budget_signal: str

    @classmethod
    def from_payload(cls, payload: PhaseTracePayload) -> "PhaseTraceTransit":
        return cls(
            phase=payload.phase,
            status=payload.status,
            duration_ms=payload.duration_ms,
            budget_signal=payload.budget_signal,
        )


@dataclass(frozen=True)
class KernelTracePhaseTransit:
    payload: dict[str, Any]

    @classmethod
    def from_payload(cls, payload: KernelTracePhaseEntryPayload) -> "KernelTracePhaseTransit":
        return cls(payload=payload.payload)


@dataclass(frozen=True)
class KernelTraceTransit:
    source_path: Path
    raw_text: str
    trace_text: KernelTraceTextTransit
    json_lines: JSONLinesTransit
    payload: KernelTracePayload

    def phase_entries(self) -> list[KernelTraceEntryPayload]:
        return [entry for entry in self.payload.entries if entry.event == "phase_trace"]


@dataclass(frozen=True)
class KernelFixtureChapterTransit:
    chapter_id: str
    chapter_mapping: "KernelFixtureChapterMappingTransit"
    payload: KernelFixtureLedgerChapterPayload

    def to_fixture_chapter(self) -> dict[str, Any]:
        chapter_meta = self.chapter_mapping.to_mapping()
        chapter_meta["status"] = "draft"
        if chapter_meta.get("lifecycle") == "frozen":
            chapter_meta["lifecycle"] = "draft"
        return chapter_meta


@dataclass(frozen=True)
class KernelFixtureChapterMappingTransit:
    payload: KernelFixtureChapterMappingPayload

    @classmethod
    def from_mapping(cls, raw_chapter: dict[str, Any]) -> "KernelFixtureChapterMappingTransit":
        return cls(payload=KernelFixtureChapterMappingPayload.model_validate(raw_chapter))

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.model_dump()


@dataclass(frozen=True)
class SDKSessionEventTransit:
    payload: SDKSessionEventPayload

    @classmethod
    def from_raw(cls, raw: dict[str, Any]) -> "SDKSessionEventTransit":
        return cls(payload=SDKSessionEventPayload.model_validate(raw))

    def event_type(self) -> str:
        return _event_type_name(self.payload.type)

    def content(self) -> str:
        data = self.payload.data
        if data is None or data.content is None:
            return ""
        return data.content

    def error_message(self) -> str:
        data = self.payload.data
        if data is None or data.message is None:
            return "unknown session error"
        return data.message


@dataclass(frozen=True)
class SDKEventObjectTransit:
    payload: SDKEventObjectPayload

    @classmethod
    def from_raw(cls, raw: dict[str, Any]) -> "SDKEventObjectTransit":
        return cls(payload=SDKEventObjectPayload.model_validate({"data": raw}))

    def mapping(self) -> dict[str, Any]:
        return self.payload.data


@dataclass(frozen=True)
class SmokeCLIArgsTransit:
    payload: SmokeCLIArgsPayload

    @classmethod
    def from_namespace(cls, namespace: argparse.Namespace) -> "SmokeCLIArgsTransit":
        return cls(payload=SmokeCLIArgsPayload.model_validate(vars(namespace)))


def _event_type_name(event_type: Any) -> str:
    value = getattr(event_type, "value", event_type)
    return str(value).strip().lower()


def _sdk_event_to_mapping(event: Any) -> dict[str, Any]:
    event_type = event.get("type") if isinstance(event, dict) else getattr(event, "type", None)
    data = event.get("data") if isinstance(event, dict) else getattr(event, "data", None)
    mapping: dict[str, Any] = {"type": event_type}
    data_mapping = data if isinstance(data, dict) else getattr(data, "__dict__", {})
    if isinstance(data_mapping, dict):
        data_transit = SDKEventObjectTransit.from_raw(data_mapping)
        mapping["data"] = {
            key: value for key, value in data_transit.mapping().items() if not str(key).startswith("_")
        }
    return mapping


async def run_ping_mode() -> int:
    sdk = importlib.import_module("copilot")
    copilot_client_cls = getattr(sdk, "CopilotClient")
    client = copilot_client_cls()
    try:
        await client.start()
        response = await client.ping("health check")
    except Exception as exc:
        print(f"FAIL: ping failed: {exc}")
        return 1
    finally:
        try:
            await client.stop()
        except Exception:
            pass

    print("PASS: Copilot SDK ping succeeded")
    print(f"response={response}")
    return 0


async def run_prompt_mode(model: str, prompt: str, timeout_s: float) -> int:
    result: dict[str, Any] = {"content": None, "error": None}
    sdk = importlib.import_module("copilot")
    copilot_client_cls = getattr(sdk, "CopilotClient")
    client = copilot_client_cls()
    session: Any | None = None

    try:
        await client.start()
        session = await client.create_session({"model": model, "streaming": False})
        assert session is not None
        response = await session.send_and_wait({"prompt": prompt}, timeout=timeout_s)
        if response is None:
            print(f"FAIL: prompt mode timed out after {timeout_s:.1f}s")
            return 1
        try:
            response_transit = SDKSessionEventTransit.from_raw(_sdk_event_to_mapping(response))
        except ValidationError as exc:
            print(f"FAIL: invalid prompt response payload: {exc}")
            return 1
        response_type = response_transit.event_type()
        if response_type in {"session.error", "sessioneventtype.session_error"}:
            result["error"] = response_transit.error_message()
        elif response_type in {"assistant.message", "sessioneventtype.assistant_message"}:
            result["content"] = response_transit.content()
        else:
            events = await session.get_messages()
            for event in reversed(events):
                try:
                    event_transit = SDKSessionEventTransit.from_raw(_sdk_event_to_mapping(event))
                except ValidationError as exc:
                    print(f"FAIL: invalid prompt session event payload: {exc}")
                    return 1
                event_type = event_transit.event_type()
                if event_type in {"assistant.message", "sessioneventtype.assistant_message"}:
                    result["content"] = event_transit.content()
                    break
                if event_type in {"session.error", "sessioneventtype.session_error"}:
                    result["error"] = event_transit.error_message()
                    break
    except TimeoutError:
        print(f"FAIL: prompt mode timed out after {timeout_s:.1f}s")
        return 1
    except Exception as exc:
        print(f"FAIL: prompt mode failed: {exc}")
        return 1
    finally:
        if session is not None:
            try:
                await session.destroy()
            except Exception:
                pass
        try:
            await client.stop()
        except Exception:
            pass

    if result["error"]:
        print(f"FAIL: session.error: {result['error']}")
        return 1

    content = str(result["content"] or "").strip()
    if not content:
        print("FAIL: empty assistant response")
        return 1

    print("PASS: Copilot SDK prompt round-trip succeeded")
    print(f"content={content!r}")
    return 0


def _load_kernel_fixture_chapter(chapter_id: str) -> KernelFixtureChapterTransit:
    ledger_transit = _load_kernel_fixture_ledger(REPO_ROOT / "state" / "ledger.json")
    chapter_payload = ledger_transit.payload.chapters.get(chapter_id)
    raw_chapter = ledger_transit.raw.get("chapters", {}).get(chapter_id)
    if chapter_payload is None or not isinstance(raw_chapter, dict):
        raise RuntimeError(f"Unknown chapter_id for fixture: {chapter_id}")
    try:
        chapter_mapping = KernelFixtureChapterMappingTransit.from_mapping(raw_chapter)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid chapter mapping payload for fixture {chapter_id}: {exc}") from exc
    return KernelFixtureChapterTransit(chapter_id=chapter_id, chapter_mapping=chapter_mapping, payload=chapter_payload)


def _load_kernel_fixture_ledger(path: Path) -> KernelFixtureLedgerTransit:
    try:
        json_mapping = _load_json_mapping(path)
    except RuntimeError as exc:
        raise RuntimeError(f"Invalid ledger JSON for fixture: {exc}") from exc
    try:
        payload = KernelFixtureLedgerPayload.model_validate(json_mapping.to_mapping())
    except ValidationError as exc:
        raise RuntimeError(f"Invalid ledger payload for fixture: {exc}") from exc
    return KernelFixtureLedgerTransit(json_mapping=json_mapping, raw=json_mapping.to_mapping(), payload=payload)


def _load_json_mapping(path: Path) -> JSONMappingTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"JSON file not found at {path}") from exc
    try:
        json_text = JSONTextTransit(source_path=path, payload=JSONTextPayload.model_validate({"text": raw_text}))
    except ValidationError as exc:
        raise RuntimeError(f"Invalid JSON text payload at {path}: {exc}") from exc
    try:
        raw = json.loads(json_text.to_text())
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON at {path}: {exc}") from exc
    try:
        payload = JSONMappingPayload.model_validate({"data": raw})
    except ValidationError as exc:
        raise RuntimeError(f"Invalid JSON mapping payload at {path}: {exc}") from exc
    return JSONMappingTransit(source_path=path, raw_text=json_text.to_text(), json_text=json_text, payload=payload)


def _build_trace_summary_fixture(
    chapter_id: str,
    fixture_root: Path,
    malformed_phase_trace: bool = False,
    non_object_phase_payload: bool = False,
    omit_evaluation_phase_trace: bool = False,
) -> tuple[Path, Path]:
    fixture_repo_root = fixture_root / "repo"
    metrics_path = fixture_repo_root / "state" / "metrics.json"
    trace_path = fixture_repo_root / "state" / "role_io" / chapter_id / "iter_01" / "out" / "kernel_trace.jsonl"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)

    metrics_payload = {
        "chapters": {
            chapter_id: {
                "history": [
                    {
                        "iteration": 1,
                        "trace_summary": {
                            "decision": "accept",
                            "drift_score": 0.0,
                            "diff_ratio": 0.0,
                            "deterministic_pass": True,
                        },
                    }
                ]
            }
        }
    }
    metrics_path.write_text(json.dumps(metrics_payload, indent=2), encoding="utf-8")

    phase_entries = [
        {"event": "phase_trace", "payload": {"phase": "role_output_ready", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
        {"event": "phase_trace", "payload": {"phase": "evaluation", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
        {"event": "phase_trace", "payload": {"phase": "state_persistence", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
    ]
    if malformed_phase_trace:
        phase_entries[1]["payload"].pop("budget_signal", None)
    if non_object_phase_payload:
        phase_entries[1]["payload"] = "not-an-object"
    if omit_evaluation_phase_trace:
        phase_entries = [entry for entry in phase_entries if entry.get("payload", {}).get("phase") != "evaluation"]
    trace_path.write_text("\n".join(json.dumps(entry) for entry in phase_entries) + "\n", encoding="utf-8")
    return metrics_path, fixture_repo_root


def _build_trace_summary_kernel_fixture(chapter_id: str, fixture_root: Path) -> tuple[Path, Path]:
    fixture_repo_root = fixture_root / "kernel_repo"
    if fixture_repo_root.exists():
        shutil.rmtree(fixture_repo_root)
    fixture_repo_root.mkdir(parents=True, exist_ok=True)

    chapter_transit = _load_kernel_fixture_chapter(chapter_id)
    chapter_meta = chapter_transit.to_fixture_chapter()
    chapter_path = chapter_transit.payload.path

    (fixture_repo_root / "state").mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / "state" / "kernel.py", fixture_repo_root / "state" / "kernel.py")
    shutil.copy2(REPO_ROOT / "state" / "llm_client.py", fixture_repo_root / "state" / "llm_client.py")
    shutil.copytree(REPO_ROOT / "evals", fixture_repo_root / "evals")
    shutil.copytree(REPO_ROOT / "prompts", fixture_repo_root / "prompts")
    shutil.copy2(REPO_ROOT / "AGENTS.md", fixture_repo_root / "AGENTS.md")
    shutil.copy2(REPO_ROOT / "CONSTITUTION.md", fixture_repo_root / "CONSTITUTION.md")
    shutil.copy2(REPO_ROOT / "ROADMAP.md", fixture_repo_root / "ROADMAP.md")
    chapter_file = fixture_repo_root / chapter_path
    chapter_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / chapter_path, chapter_file)

    fixture_ledger = {"chapters": {chapter_id: chapter_meta}, "repo_iteration_log": []}
    (fixture_repo_root / "state" / "ledger.json").write_text(json.dumps(fixture_ledger, indent=2) + "\n", encoding="utf-8")
    (fixture_repo_root / "state" / "metrics.json").write_text(json.dumps({"chapters": {}}, indent=2) + "\n", encoding="utf-8")
    source_version_map = REPO_ROOT / "state" / "version_map.json"
    if source_version_map.exists():
        shutil.copy2(source_version_map, fixture_repo_root / "state" / "version_map.json")
    else:
        (fixture_repo_root / "state" / "version_map.json").write_text("{}\n", encoding="utf-8")

    subprocess.run(["git", "init"], cwd=fixture_repo_root, check=True, capture_output=True, text=True)
    subprocess.run(["git", "add", "."], cwd=fixture_repo_root, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "-c", "user.name=trace-smoke", "-c", "user.email=trace-smoke@example.com", "commit", "-m", "fixture"],
        cwd=fixture_repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return fixture_repo_root / "state" / "metrics.json", fixture_repo_root


def _load_metrics(path: Path) -> MetricsTransit:
    try:
        json_mapping = _load_json_mapping(path)
    except RuntimeError as exc:
        raise RuntimeError(f"Invalid metrics JSON at {path}: {exc}") from exc
    try:
        payload = MetricsPayload.model_validate(json_mapping.to_mapping())
    except ValidationError as exc:
        raise RuntimeError(f"Invalid metrics payload at {path}: {exc}") from exc
    return MetricsTransit(json_mapping=json_mapping, raw=json_mapping.to_mapping(), payload=payload)


def _load_kernel_trace(path: Path) -> KernelTraceTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Kernel trace file not found: {path}") from exc
    try:
        trace_text_payload = KernelTraceTextPayload.model_validate({"text": raw_text})
    except ValidationError as exc:
        raise RuntimeError(f"Invalid kernel trace text payload at {path}: {exc}") from exc
    trace_text_transit = KernelTraceTextTransit(source_path=path, payload=trace_text_payload)
    raw_entries: list[dict[str, Any]] = []
    for line_number, line in enumerate(trace_text_transit.lines(), start=1):
        if not line.strip():
            continue
        try:
            line_text = JSONLineTextTransit.from_line(line_number=line_number, text=line)
        except ValidationError as exc:
            raise RuntimeError(f"Invalid kernel trace line text payload at {path}:{line_number}: {exc}") from exc
        try:
            parsed_line = json.loads(line_text.to_text())
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid kernel trace entry JSON at {path}:{line_text.line_number}: {exc}") from exc
        if not isinstance(parsed_line, dict):
            raise RuntimeError(f"Invalid kernel trace entry JSON at {path}:{line_text.line_number}: expected object mapping")
        try:
            line_transit = JSONLineTransit.from_mapping(line_number=line_text.line_number, parsed_line=parsed_line)
        except ValidationError as exc:
            raise RuntimeError(f"Invalid kernel trace line payload at {path}:{line_text.line_number}: {exc}") from exc
        raw_entries.append(line_transit.to_mapping())
    try:
        json_lines_payload = JSONLinesPayload.model_validate({"entries": raw_entries})
    except ValidationError as exc:
        raise RuntimeError(f"Invalid kernel trace JSON mapping payload at {path}: {exc}") from exc
    json_lines = JSONLinesTransit.from_payload(json_lines_payload)
    try:
        payload = KernelTracePayload.model_validate({"entries": json_lines.to_mappings()})
    except ValidationError as exc:
        raise RuntimeError(f"Invalid kernel trace payload at {path}: {exc}") from exc
    return KernelTraceTransit(
        source_path=path,
        raw_text=trace_text_transit.payload.text,
        trace_text=trace_text_transit,
        json_lines=json_lines,
        payload=payload,
    )


async def run_trace_summary_mode(
    chapter_id: str,
    max_iterations: int,
    run_kernel: bool,
    metrics_path: Path,
    fixture_root: Path,
    expect_phase_trace_failure: bool = False,
    inject_malformed_phase_trace: bool = False,
    inject_non_object_phase_payload: bool = False,
    inject_missing_required_phase_trace: bool = False,
) -> int:
    repo_root_for_trace = REPO_ROOT
    metrics_path_for_trace = metrics_path
    fixture_cleanup_target: Path | None = None
    if run_kernel:
        metrics_path_for_trace, repo_root_for_trace = _build_trace_summary_kernel_fixture(
            chapter_id=chapter_id,
            fixture_root=fixture_root,
        )
    else:
        metrics_path_for_trace, repo_root_for_trace = _build_trace_summary_fixture(
            chapter_id=chapter_id,
            fixture_root=fixture_root,
            malformed_phase_trace=inject_malformed_phase_trace,
            non_object_phase_payload=inject_non_object_phase_payload,
            omit_evaluation_phase_trace=inject_missing_required_phase_trace,
        )
    fixture_cleanup_target = repo_root_for_trace

    try:
        if run_kernel:
            fixture_kernel_path = repo_root_for_trace / "state" / "kernel.py"
            kernel_cmd = [
                sys.executable,
                str(fixture_kernel_path),
                "--chapter-id",
                chapter_id,
                "--llm",
                "--llm-provider",
                "mock",
                "--max-iterations",
                str(max_iterations),
            ]
            proc = subprocess.run(kernel_cmd, cwd=repo_root_for_trace, capture_output=True, text=True)
            if proc.returncode not in {0, 1}:
                print("FAIL: kernel run failed for trace-summary smoke")
                if proc.stdout:
                    print(proc.stdout.strip())
                if proc.stderr:
                    print(proc.stderr.strip())
                return 1

        metrics_transit = _load_metrics(metrics_path_for_trace)
        chapter_metrics = metrics_transit.payload.chapters.get(chapter_id)
        if chapter_metrics is None or not chapter_metrics.history:
            print(f"FAIL: no metrics history for chapter {chapter_id}")
            return 1

        latest_entry = chapter_metrics.history[-1]
        latest = MetricsHistoryTransit(iteration=latest_entry.iteration, trace_summary=latest_entry.trace_summary)
        trace_summary = TraceSummaryTransit.from_payload(latest.trace_summary).to_mapping()

        required_keys = {"decision", "drift_score", "diff_ratio", "deterministic_pass"}
        missing = sorted(required_keys - set(trace_summary))
        if missing:
            print(f"FAIL: trace_summary missing keys: {missing}")
            return 1

        iteration = latest.iteration
        trace_path = repo_root_for_trace / "state" / "role_io" / chapter_id / f"iter_{iteration:02d}" / "out" / "kernel_trace.jsonl"
        if not trace_path.exists():
            print(f"FAIL: kernel trace file missing at {trace_path}")
            return 1

        try:
            trace_transit = _load_kernel_trace(trace_path)
        except RuntimeError as exc:
            print(f"FAIL: {exc}")
            return 1
        phase_entries = trace_transit.phase_entries()
        if run_kernel and phase_entries:
            if inject_malformed_phase_trace:
                payload = phase_entries[0].payload
                if isinstance(payload, dict):
                    payload.pop("budget_signal", None)
            if inject_non_object_phase_payload:
                phase_entries[0].payload = "not-an-object"
            if inject_missing_required_phase_trace:
                phase_entries = [
                    entry
                    for entry in phase_entries
                    if not (isinstance(entry.payload, dict) and entry.payload.get("phase") == "evaluation")
                ]
        phase_transits: list[PhaseTraceTransit] = []
        phase_entry_transits: list[KernelTracePhaseTransit] = []
        if not phase_entries:
            observed_phase_trace_failure = "no phase_trace events in kernel trace"
        else:
            observed_phase_trace_failure = ""

        if not observed_phase_trace_failure:
            for entry in phase_entries:
                try:
                    phase_entry_transits.append(
                        KernelTracePhaseTransit.from_payload(
                            KernelTracePhaseEntryPayload.model_validate(
                                {"event": entry.event, "payload": entry.payload}
                            )
                        )
                    )
                    phase_transits.append(
                        PhaseTraceTransit.from_payload(
                            PhaseTracePayload.model_validate(phase_entry_transits[-1].payload)
                        )
                    )
                except ValidationError as exc:
                    missing_keys = sorted(
                        {
                            ".".join(str(part) for part in error["loc"])
                            for error in exc.errors()
                            if error.get("type") == "missing"
                        }
                    )
                    if missing_keys:
                        observed_phase_trace_failure = f"phase_trace missing keys: {missing_keys}"
                    else:
                        observed_phase_trace_failure = "phase_trace payload is not an object"
                    break

        if not observed_phase_trace_failure:
            phase_names = {entry.phase for entry in phase_transits}
            required_phases = {"role_output_ready", "evaluation", "state_persistence"}
            missing_phases = sorted(required_phases - phase_names)
            if missing_phases:
                observed_phase_trace_failure = f"missing required phase traces: {missing_phases}"

        if expect_phase_trace_failure:
            if observed_phase_trace_failure:
                print(f"PASS: expected phase_trace validation failure observed: {observed_phase_trace_failure}")
                return 0
            print("FAIL: expected malformed phase_trace validation failure, but validation passed")
            return 1

        if observed_phase_trace_failure:
            print(f"FAIL: {observed_phase_trace_failure}")
            return 1

        print("PASS: trace_summary present with required keys")
        print(f"trace_summary={trace_summary}")
        print(f"phase_trace_events={len(phase_transits)}")
        return 0
    finally:
        if fixture_cleanup_target is not None and fixture_cleanup_target.exists():
            shutil.rmtree(fixture_cleanup_target)


async def main_async(args: SmokeCLIArgsTransit) -> int:
    cli_args = args.payload
    if cli_args.mode == "ping":
        return await run_ping_mode()
    if cli_args.mode == "prompt":
        return await run_prompt_mode(model=cli_args.model, prompt=cli_args.prompt, timeout_s=cli_args.timeout)
    mode_spec = TRACE_SUMMARY_MODE_SPECS.get(cli_args.mode)
    if mode_spec is None:
        return await run_trace_summary_mode(
            chapter_id=cli_args.chapter_id,
            max_iterations=cli_args.kernel_max_iterations,
            run_kernel=cli_args.run_kernel_for_trace_summary,
            metrics_path=Path(cli_args.metrics_path),
            fixture_root=Path(cli_args.trace_summary_fixture_root),
        )
    return await run_trace_summary_mode(
        chapter_id=cli_args.chapter_id,
        max_iterations=cli_args.kernel_max_iterations,
        run_kernel=cli_args.run_kernel_for_trace_summary,
        metrics_path=Path(cli_args.metrics_path),
        fixture_root=Path(cli_args.trace_summary_fixture_root),
        **mode_spec,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument(
        "--mode",
        choices=[
            "ping",
            "prompt",
            *TRACE_SUMMARY_MODE_SPECS,
        ],
        default="ping",
    )
    parser.add_argument("--model", default="gpt-5")
    parser.add_argument("--prompt", default="Reply with exactly: ok")
    parser.add_argument("--timeout", type=float, default=45.0)
    parser.add_argument("--chapter-id", default="01-paradigm-shift")
    parser.add_argument("--kernel-max-iterations", type=int, default=1)
    parser.add_argument("--run-kernel-for-trace-summary", action="store_true")
    parser.add_argument("--metrics-path", default=str(METRICS_PATH))
    parser.add_argument("--trace-summary-fixture-root", default=str(TRACE_SUMMARY_FIXTURE_ROOT))
    args = parser.parse_args()
    try:
        args_transit = SmokeCLIArgsTransit.from_namespace(args)
    except ValidationError as exc:
        print(f"FAIL: invalid CLI args payload: {exc}")
        return 1
    return asyncio.run(main_async(args_transit))


if __name__ == "__main__":
    raise SystemExit(main())
