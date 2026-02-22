#!/usr/bin/env python3
"""Operational governance utilities for state/ledger.json.

This repo uses the ledger as a control surface, not a passive log.
The engine here is intentionally minimal:
- Deterministic chapter selection (prevents oscillation)
- Invariant checks (locks, schema, governance file modifications)
- Lifecycle transition computation (draft -> refined)

It does not attempt to run evals or write content.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError


LEDGER_DEFAULT_PATH = Path(__file__).resolve().parent / "ledger.json"
IMMUTABLE_GOVERNANCE_FILES = {"AGENTS.md", "CONSTITUTION.md"}


class GovernanceError(RuntimeError):
    pass


class ChapterQualityPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    structure_score: float | int | None = 0.0
    drift_score: float | int | None = 0.0


class ChapterStabilityPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    consecutive_passes: int | None = 0
    last_modified_iteration: int | str | None = 0
    frozen_candidate: bool | None = None


class LedgerChapterPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    status: str | None = None
    lifecycle: str | None = None
    quality_metrics: ChapterQualityPayload = Field(default_factory=ChapterQualityPayload)
    stability: ChapterStabilityPayload = Field(default_factory=ChapterStabilityPayload)


class DraftToRefinedTransitionPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    required_consecutive_passes: int | None = 2


class LifecycleTransitionsPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    draft_to_refined: DraftToRefinedTransitionPayload = Field(default_factory=DraftToRefinedTransitionPayload)


class ChapterLifecycleRulesPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    transitions: LifecycleTransitionsPayload = Field(default_factory=LifecycleTransitionsPayload)


class ChapterSelectionStrategyPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    lifecycle_priority: list[str] = Field(default_factory=list)


class GovernanceCLIArgsPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cmd: Literal["validate", "select", "promotions", "unhold", "unlock"]
    ledger: Path
    chapter_id: list[str] = Field(default_factory=list)
    status: str = "active_refinement"


class ChapterStatusUpdatePayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    chapter_id: list[str]
    status: str


class LedgerPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    version: int | None = None
    chapter_lifecycle_rules: ChapterLifecycleRulesPayload = Field(default_factory=ChapterLifecycleRulesPayload)
    chapter_selection_strategy: ChapterSelectionStrategyPayload = Field(default_factory=ChapterSelectionStrategyPayload)
    repo_iteration_log: list[dict[str, Any]] = Field(default_factory=list)
    chapters: dict[str, LedgerChapterPayload] = Field(default_factory=dict)


class LedgerJSONPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: dict[str, Any]


class JSONTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


@dataclass(frozen=True)
class JSONTextTransit:
    source_path: Path
    payload: JSONTextPayload

    def to_text(self) -> str:
        return self.payload.text


@dataclass(frozen=True)
class LedgerJSONTransit:
    source_path: Path
    raw_text: str
    json_text: JSONTextTransit
    payload: LedgerJSONPayload

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.data


@dataclass(frozen=True)
class LedgerTransit:
    json_mapping: LedgerJSONTransit
    raw: dict[str, Any]
    payload: LedgerPayload

    def as_ledger_dict(self) -> dict[str, Any]:
        return self.raw


@dataclass(frozen=True)
class PromotionRulesTransit:
    required_consecutive_passes: int

    @classmethod
    def from_payload(cls, payload: ChapterLifecycleRulesPayload) -> "PromotionRulesTransit":
        required = payload.transitions.draft_to_refined.required_consecutive_passes
        return cls(required_consecutive_passes=int(required if required is not None else 2))


@dataclass(frozen=True)
class SelectionStrategyTransit:
    lifecycle_priority: tuple[str, ...]

    @classmethod
    def from_payload(cls, payload: ChapterSelectionStrategyPayload) -> "SelectionStrategyTransit":
        lifecycle_priority = tuple(item for item in payload.lifecycle_priority if isinstance(item, str) and item.strip())
        return cls(lifecycle_priority=lifecycle_priority)


@dataclass(frozen=True)
class GovernanceCLIArgsTransit:
    payload: GovernanceCLIArgsPayload

    @classmethod
    def from_namespace(cls, args: argparse.Namespace) -> "GovernanceCLIArgsTransit":
        chapter_ids = getattr(args, "chapter_id", [])
        if not isinstance(chapter_ids, list):
            chapter_ids = []
        payload = GovernanceCLIArgsPayload.model_validate(
            {
                "cmd": str(args.cmd),
                "ledger": Path(args.ledger),
                "chapter_id": [str(chapter_id) for chapter_id in chapter_ids],
                "status": str(getattr(args, "status", "active_refinement")),
            }
        )
        return cls(payload=payload)

    def to_namespace(self) -> argparse.Namespace:
        return argparse.Namespace(
            cmd=self.payload.cmd,
            ledger=self.payload.ledger,
            chapter_id=list(self.payload.chapter_id),
            status=self.payload.status,
        )


@dataclass(frozen=True)
class ChapterStatusUpdateTransit:
    payload: ChapterStatusUpdatePayload

    @classmethod
    def from_namespace(cls, args: argparse.Namespace) -> "ChapterStatusUpdateTransit":
        return cls(
            payload=ChapterStatusUpdatePayload.model_validate(
                {
                    "chapter_id": [str(chapter_id) for chapter_id in getattr(args, "chapter_id", [])],
                    "status": str(getattr(args, "status", "active_refinement")),
                }
            )
        )


def _load_json(path: Path) -> LedgerJSONTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise GovernanceError(f"Ledger not found: {path}") from exc
    try:
        json_text = JSONTextTransit(source_path=path, payload=JSONTextPayload.model_validate({"text": raw_text}))
    except ValidationError as exc:
        raise GovernanceError(f"Invalid ledger JSON text payload at {path}: {exc}") from exc
    try:
        parsed = json.loads(json_text.to_text())
    except json.JSONDecodeError as exc:
        raise GovernanceError(f"Invalid JSON in ledger: {path}: {exc}") from exc
    try:
        payload = LedgerJSONPayload.model_validate({"data": parsed})
    except ValidationError as exc:
        raise GovernanceError(f"Invalid ledger JSON payload root at {path}: {exc}") from exc
    return LedgerJSONTransit(source_path=path, raw_text=json_text.to_text(), json_text=json_text, payload=payload)


def _dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def _save_json(path: Path, data: Any) -> None:
    path.write_text(_dump_json(data) + "\n", encoding="utf-8")


def _load_ledger(path: Path) -> LedgerTransit:
    json_mapping = _load_json(path)
    raw = json_mapping.to_mapping()
    try:
        payload = LedgerPayload.model_validate(raw)
    except ValidationError as exc:
        raise GovernanceError(f"Invalid ledger payload: {exc}") from exc
    return LedgerTransit(json_mapping=json_mapping, raw=raw, payload=payload)


def _get_chapters(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    chapters = ledger.get("chapters")
    if not isinstance(chapters, dict):
        raise GovernanceError("ledger.chapters must be an object")
    return chapters  # type: ignore[return-value]


def _require_fields(obj: dict[str, Any], fields: Iterable[str], ctx: str) -> None:
    for field in fields:
        if field not in obj:
            raise GovernanceError(f"Missing required field {ctx}.{field}")


def validate_ledger(ledger: dict[str, Any]) -> list[str]:
    """Return a list of validation errors (empty means pass)."""

    errors: list[str] = []

    def capture(fn, *args, **kwargs):
        try:
            fn(*args, **kwargs)
        except GovernanceError as exc:
            errors.append(str(exc))

    capture(_validate_top_level, ledger)
    capture(_validate_repo_iteration_log, ledger)
    capture(_validate_chapters, ledger)

    return errors


def _validate_top_level(ledger: dict[str, Any]) -> None:
    version = ledger.get("version")
    if version != 2:
        raise GovernanceError(f"ledger.version must be 2 (found {version!r})")

    if "chapter_lifecycle_rules" not in ledger:
        raise GovernanceError("Missing ledger.chapter_lifecycle_rules")
    if "chapter_selection_strategy" not in ledger:
        raise GovernanceError("Missing ledger.chapter_selection_strategy")


def _validate_repo_iteration_log(ledger: dict[str, Any]) -> None:
    repo_log = ledger.get("repo_iteration_log")
    if not isinstance(repo_log, list):
        raise GovernanceError("ledger.repo_iteration_log must be an array")

    for entry in repo_log:
        if not isinstance(entry, dict):
            raise GovernanceError("repo_iteration_log entries must be objects")

        _require_fields(entry, ["iteration", "timestamp", "agent_task", "inputs", "evals", "outcome", "artifacts"], "repo_iteration_log[]")

        scope = entry.get("scope")
        if not isinstance(scope, dict):
            raise GovernanceError("repo_iteration_log[].scope must be an object")
        _require_fields(scope, ["chapters_modified", "patterns_modified", "governance_modified"], "repo_iteration_log[].scope")

        resource_usage = entry.get("resource_usage")
        if not isinstance(resource_usage, dict):
            raise GovernanceError("repo_iteration_log[].resource_usage must be an object")
        _require_fields(resource_usage, ["prompt_tokens", "completion_tokens", "eval_runtime_ms"], "repo_iteration_log[].resource_usage")

        changed_files = entry.get("inputs", {}).get("changed_files")
        if not isinstance(changed_files, list):
            raise GovernanceError("repo_iteration_log[].inputs.changed_files must be an array")

        iteration = entry.get("iteration")
        if isinstance(iteration, int) and iteration > 1:
            if any(f in IMMUTABLE_GOVERNANCE_FILES for f in changed_files):
                raise GovernanceError(
                    "Immutable governance files were modified after iteration 1: "
                    + ", ".join(sorted(set(changed_files) & IMMUTABLE_GOVERNANCE_FILES))
                )

        governance_modified = scope.get("governance_modified")
        if any(f in IMMUTABLE_GOVERNANCE_FILES for f in changed_files) and governance_modified is not True:
            raise GovernanceError("governance_modified must be true when governance files are in changed_files")


def _validate_chapters(ledger: dict[str, Any]) -> None:
    chapters = _get_chapters(ledger)
    if not chapters:
        raise GovernanceError("ledger.chapters must not be empty")

    for chapter_id, chapter in chapters.items():
        if not isinstance(chapter, dict):
            raise GovernanceError(f"chapters.{chapter_id} must be an object")

        _require_fields(
            chapter,
            [
                "path",
                "status",
                "lifecycle",
                "current_iteration",
                "revision_count",
                "last_eval",
                "quality_metrics",
                "stability",
                "drift_history",
                "research",
                "human_validation",
                "iteration_log",
            ],
            f"chapters.{chapter_id}",
        )

        quality_metrics = chapter.get("quality_metrics")
        if not isinstance(quality_metrics, dict):
            raise GovernanceError(f"chapters.{chapter_id}.quality_metrics must be an object")
        _require_fields(
            quality_metrics,
            [
                "structure_score",
                "clarity_score",
                "example_density",
                "tradeoff_presence",
                "failure_mode_presence",
                "drift_score",
            ],
            f"chapters.{chapter_id}.quality_metrics",
        )

        stability = chapter.get("stability")
        if not isinstance(stability, dict):
            raise GovernanceError(f"chapters.{chapter_id}.stability must be an object")
        _require_fields(stability, ["consecutive_passes", "last_modified_iteration", "frozen_candidate"], f"chapters.{chapter_id}.stability")

        research = chapter.get("research")
        if not isinstance(research, dict):
            raise GovernanceError(f"chapters.{chapter_id}.research must be an object")
        _require_fields(research, ["hypothesis", "falsifiable", "validation_status"], f"chapters.{chapter_id}.research")
        if research.get("validation_status") not in {"untested", "validated", "falsified"}:
            raise GovernanceError(
                f"chapters.{chapter_id}.research.validation_status must be one of untested|validated|falsified"
            )

        human_validation = chapter.get("human_validation")
        if not isinstance(human_validation, dict):
            raise GovernanceError(f"chapters.{chapter_id}.human_validation must be an object")
        _require_fields(human_validation, ["approved", "approved_by", "approved_at"], f"chapters.{chapter_id}.human_validation")


@dataclass(frozen=True)
class ChapterKey:
    chapter_id: str
    lifecycle: str
    structure_score: float
    drift_score: float
    last_modified_iteration: int


def _is_chapter_eligible(chapter: dict[str, Any]) -> bool:
    status = chapter.get("status")
    lifecycle = chapter.get("lifecycle")

    if status in {"locked"}:
        return False
    if lifecycle == "frozen":
        return False
    return True


def select_next_chapter_id(ledger: dict[str, Any], strategy: SelectionStrategyTransit | None = None) -> str:
    """Select the next chapter deterministically per ledger.chapter_selection_strategy."""

    chapters = _get_chapters(ledger)
    candidates: list[ChapterKey] = []

    for chapter_id, chapter in chapters.items():
        if not _is_chapter_eligible(chapter):
            continue

        quality = chapter.get("quality_metrics", {})
        stability = chapter.get("stability", {})

        lifecycle = str(chapter.get("lifecycle") or "draft")
        try:
            structure_score = float(quality.get("structure_score", 0.0))
        except (TypeError, ValueError):
            structure_score = 0.0
        try:
            drift_score = float(quality.get("drift_score", 0.0))
        except (TypeError, ValueError):
            drift_score = 0.0

        last_modified_iteration_raw = stability.get("last_modified_iteration", 0)
        try:
            last_modified_iteration = int(last_modified_iteration_raw)
        except (TypeError, ValueError):
            last_modified_iteration = 0

        candidates.append(
            ChapterKey(
                chapter_id=chapter_id,
                lifecycle=lifecycle,
                structure_score=structure_score,
                drift_score=drift_score,
                last_modified_iteration=last_modified_iteration,
            )
        )

    if not candidates:
        raise GovernanceError("No eligible chapters found (all locked/frozen?)")

    configured_order = strategy.lifecycle_priority if strategy is not None else ()
    if configured_order:
        lifecycle_rank_map = {name: idx for idx, name in enumerate(configured_order)}
    else:
        lifecycle_rank_map = {"draft": 0, "refined": 1, "approved": 2, "frozen": 3}

    def lifecycle_rank(lifecycle: str) -> int:
        return lifecycle_rank_map.get(lifecycle, 99)

    # Priority:
    # 1) lifecycle == draft
    # 2) lowest structure_score
    # 3) highest drift_score
    # 4) oldest last_modified_iteration
    candidates.sort(
        key=lambda c: (
            lifecycle_rank(c.lifecycle),
            c.structure_score,
            -c.drift_score,
            c.last_modified_iteration,
            c.chapter_id,
        )
    )

    return candidates[0].chapter_id


def compute_lifecycle_promotions(
    ledger: dict[str, Any],
    rules_transit: PromotionRulesTransit | None = None,
) -> dict[str, str]:
    """Compute draft->refined promotions from consecutive passes.

    Returns a mapping of chapter_id -> new_lifecycle for chapters that should change.
    """

    required_passes_int = rules_transit.required_consecutive_passes if rules_transit is not None else 2
    if rules_transit is None:
        rules = ledger.get("chapter_lifecycle_rules", {})
        transitions = rules.get("transitions", {}) if isinstance(rules, dict) else {}
        draft_to_refined = transitions.get("draft_to_refined", {}) if isinstance(transitions, dict) else {}
        required_passes = draft_to_refined.get("required_consecutive_passes", 2)
        try:
            required_passes_int = int(required_passes)
        except (TypeError, ValueError):
            required_passes_int = 2

    chapters = _get_chapters(ledger)
    promotions: dict[str, str] = {}

    for chapter_id, chapter in chapters.items():
        if chapter.get("lifecycle") != "draft":
            continue

        stability = chapter.get("stability", {})
        consecutive_passes = stability.get("consecutive_passes", 0)
        try:
            consecutive_passes_int = int(consecutive_passes)
        except (TypeError, ValueError):
            consecutive_passes_int = 0

        if consecutive_passes_int >= required_passes_int:
            promotions[chapter_id] = "refined"

    return promotions


def _cmd_validate(args: argparse.Namespace) -> int:
    ledger = _load_ledger(args.ledger).as_ledger_dict()
    errors = validate_ledger(ledger)
    if errors:
        sys.stderr.write("Ledger validation failed:\n")
        for err in errors:
            sys.stderr.write(f"- {err}\n")
        return 1

    sys.stdout.write("Ledger validation: pass\n")
    return 0


def _cmd_select(args: argparse.Namespace) -> int:
    ledger_transit = _load_ledger(args.ledger)
    ledger = ledger_transit.as_ledger_dict()
    errors = validate_ledger(ledger)
    if errors:
        sys.stderr.write("Ledger validation failed; refusing to select.\n")
        for err in errors:
            sys.stderr.write(f"- {err}\n")
        return 1

    strategy_transit = SelectionStrategyTransit.from_payload(ledger_transit.payload.chapter_selection_strategy)
    chapter_id = select_next_chapter_id(ledger, strategy=strategy_transit)
    sys.stdout.write(chapter_id + "\n")
    return 0


def _cmd_promotions(args: argparse.Namespace) -> int:
    ledger_transit = _load_ledger(args.ledger)
    ledger = ledger_transit.as_ledger_dict()
    errors = validate_ledger(ledger)
    if errors:
        sys.stderr.write("Ledger validation failed; refusing to compute promotions.\n")
        for err in errors:
            sys.stderr.write(f"- {err}\n")
        return 1

    rules_transit = PromotionRulesTransit.from_payload(ledger_transit.payload.chapter_lifecycle_rules)
    promotions = compute_lifecycle_promotions(ledger, rules_transit=rules_transit)
    sys.stdout.write(_dump_json(promotions) + "\n")
    return 0


def _cmd_unhold(args: argparse.Namespace) -> int:
    try:
        status_update = ChapterStatusUpdateTransit.from_namespace(args)
    except ValidationError as exc:
        raise GovernanceError(f"Invalid status update payload: {exc}") from exc
    ledger_transit = _load_ledger(args.ledger)
    ledger = ledger_transit.as_ledger_dict()
    errors = validate_ledger(ledger)
    if errors:
        sys.stderr.write("Ledger validation failed; refusing to unhold.\n")
        for err in errors:
            sys.stderr.write(f"- {err}\n")
        return 1

    new_status = status_update.payload.status
    if new_status in {"hold", "locked"}:
        sys.stderr.write("Refusing to set status to hold/locked; choose an eligible status.\n")
        return 2

    chapters = _get_chapters(ledger)
    changed = 0
    for chapter_id in status_update.payload.chapter_id:
        if chapter_id not in chapters:
            sys.stderr.write(f"Unknown chapter_id: {chapter_id}\n")
            return 2
        chapter = chapters[chapter_id]
        if not isinstance(chapter, dict):
            sys.stderr.write(f"Invalid chapter payload type for {chapter_id}: expected object\n")
            return 2

        if chapter.get("status") == "hold":
            chapter["status"] = new_status
            changed += 1

    if changed:
        _save_json(args.ledger, ledger)

    sys.stdout.write(f"unhold: updated {changed} chapter(s)\n")
    return 0


def _cmd_unlock(args: argparse.Namespace) -> int:
    try:
        status_update = ChapterStatusUpdateTransit.from_namespace(args)
    except ValidationError as exc:
        raise GovernanceError(f"Invalid status update payload: {exc}") from exc
    ledger_transit = _load_ledger(args.ledger)
    ledger = ledger_transit.as_ledger_dict()
    errors = validate_ledger(ledger)
    if errors:
        sys.stderr.write("Ledger validation failed; refusing to unlock.\n")
        for err in errors:
            sys.stderr.write(f"- {err}\n")
        return 1

    new_status = status_update.payload.status
    if new_status in {"hold", "locked"}:
        sys.stderr.write("Refusing to set status to hold/locked; choose an eligible status.\n")
        return 2

    chapters = _get_chapters(ledger)
    changed = 0
    for chapter_id in status_update.payload.chapter_id:
        if chapter_id not in chapters:
            sys.stderr.write(f"Unknown chapter_id: {chapter_id}\n")
            return 2
        chapter = chapters[chapter_id]
        if not isinstance(chapter, dict):
            sys.stderr.write(f"Invalid chapter payload type for {chapter_id}: expected object\n")
            return 2

        if chapter.get("status") == "locked":
            chapter["status"] = new_status
            changed += 1

    if changed:
        _save_json(args.ledger, ledger)

    sys.stdout.write(f"unlock: updated {changed} chapter(s)\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="governance_engine", description="Operational governance utilities for state/ledger.json")
    parser.add_argument("--ledger", type=Path, default=LEDGER_DEFAULT_PATH, help="Path to ledger.json")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_validate = sub.add_parser("validate", help="Validate ledger invariants")
    p_validate.set_defaults(func=_cmd_validate)

    p_select = sub.add_parser("select", help="Select next eligible chapter deterministically")
    p_select.set_defaults(func=_cmd_select)

    p_promotions = sub.add_parser("promotions", help="Compute lifecycle promotions (draft->refined)")
    p_promotions.set_defaults(func=_cmd_promotions)

    p_unhold = sub.add_parser("unhold", help="Clear hold status for one or more chapters")
    p_unhold.add_argument("--chapter-id", nargs="+", required=True, help="Chapter id(s) to unhold")
    p_unhold.add_argument(
        "--status",
        default="active_refinement",
        help="New status to apply when current status is 'hold' (default: active_refinement)",
    )
    p_unhold.set_defaults(func=_cmd_unhold)

    p_unlock = sub.add_parser("unlock", help="Clear locked status for one or more chapters")
    p_unlock.add_argument("--chapter-id", nargs="+", required=True, help="Chapter id(s) to unlock")
    p_unlock.add_argument(
        "--status",
        default="active_refinement",
        help="New status to apply when current status is 'locked' (default: active_refinement)",
    )
    p_unlock.set_defaults(func=_cmd_unlock)

    args = parser.parse_args(argv)
    try:
        cli_args = GovernanceCLIArgsTransit.from_namespace(args)
    except ValidationError as exc:
        raise GovernanceError(f"Invalid CLI args payload: {exc}") from exc
    handler_map: dict[str, Any] = {
        "validate": _cmd_validate,
        "select": _cmd_select,
        "promotions": _cmd_promotions,
        "unhold": _cmd_unhold,
        "unlock": _cmd_unlock,
    }
    return int(handler_map[cli_args.payload.cmd](cli_args.to_namespace()))


if __name__ == "__main__":
    raise SystemExit(main())
