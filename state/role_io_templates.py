#!/usr/bin/env python3
"""Generate role I/O templates for the Planner/Writer/Critic loop.

This is intentionally minimal and deterministic. It does not run the kernel.
It only creates scaffold files under `state/role_io/<chapter-id>/iter_XX/out/`.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "state" / "ledger.json"


class TemplateError(RuntimeError):
    pass


class LedgerChapterPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    path: str
    current_iteration: int | None = None


class LedgerPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    chapters: dict[str, LedgerChapterPayload]


class JSONMappingPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: dict[str, Any]


class ChapterTextPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


@dataclass(frozen=True)
class TemplateContext:
    chapter_id: str
    iteration: int
    chapter_path: str
    chapter_text_transit: "ChapterTextTransit"

    @property
    def chapter_text(self) -> str:
        return self.chapter_text_transit.to_text()


@dataclass(frozen=True)
class LedgerTransit:
    json_mapping: JSONMappingTransit
    raw: dict[str, Any]
    payload: LedgerPayload


@dataclass(frozen=True)
class JSONMappingTransit:
    source_path: Path
    raw_text: str
    payload: JSONMappingPayload

    def to_mapping(self) -> dict[str, Any]:
        return self.payload.data


@dataclass(frozen=True)
class ChapterTextTransit:
    source_path: Path
    raw_text: str
    payload: ChapterTextPayload

    def to_text(self) -> str:
        return self.payload.text


def _load_json(path: Path) -> JSONMappingTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise TemplateError(f"Missing JSON file: {path}") from exc
    try:
        raw = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise TemplateError(f"Invalid JSON: {path}: {exc}") from exc
    try:
        payload = JSONMappingPayload.model_validate({"data": raw})
    except ValidationError as exc:
        raise TemplateError(f"Invalid JSON mapping payload: {path}: {exc}") from exc
    return JSONMappingTransit(source_path=path, raw_text=raw_text, payload=payload)


def _load_ledger(path: Path) -> LedgerTransit:
    json_mapping = _load_json(path)
    raw = json_mapping.to_mapping()
    try:
        payload = LedgerPayload.model_validate(raw)
    except ValidationError as exc:
        raise TemplateError(f"Invalid ledger payload: {exc}") from exc
    return LedgerTransit(json_mapping=json_mapping, raw=raw, payload=payload)


def _write_if_missing(path: Path, content: str, *, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _resolve_iteration(ledger: LedgerTransit, chapter_id: str, iteration: int | None) -> int:
    chapter = ledger.payload.chapters.get(chapter_id)
    if chapter is None:
        raise TemplateError(f"Unknown chapter_id: {chapter_id}")

    if iteration is not None:
        if iteration <= 0:
            raise TemplateError("--iteration must be positive")
        return iteration

    current_iteration_raw = chapter.current_iteration or 0
    try:
        current_iteration = int(current_iteration_raw)
    except (TypeError, ValueError):
        current_iteration = 0
    return current_iteration + 1


def _load_chapter_text(path: Path) -> ChapterTextTransit:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise TemplateError(f"Chapter file not found: {path}") from exc
    try:
        payload = ChapterTextPayload.model_validate({"text": raw_text})
    except ValidationError as exc:
        raise TemplateError(f"Invalid chapter text payload: {path}: {exc}") from exc
    return ChapterTextTransit(source_path=path, raw_text=raw_text, payload=payload)


def _build_template_context(ledger: LedgerTransit, chapter_id: str, iteration: int) -> TemplateContext:
    chapter = ledger.payload.chapters.get(chapter_id)
    if chapter is None:
        raise TemplateError(f"Unknown chapter_id: {chapter_id}")
    chapter_file = REPO_ROOT / chapter.path
    chapter_text_transit = _load_chapter_text(chapter_file)
    return TemplateContext(
        chapter_id=chapter_id,
        iteration=iteration,
        chapter_path=chapter.path,
        chapter_text_transit=chapter_text_transit,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="role-io-templates", description="Generate Planner/Writer/Critic template outputs")
    parser.add_argument("--chapter-id", required=True)
    parser.add_argument("--io-dir", type=Path, default=REPO_ROOT / "state" / "role_io")
    parser.add_argument("--iteration", type=int, default=None, help="Iteration number to scaffold (defaults to current_iteration+1)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")

    args = parser.parse_args(argv)

    ledger = _load_ledger(LEDGER_PATH)
    chapter_id = str(args.chapter_id)
    iteration = _resolve_iteration(ledger, chapter_id, args.iteration)
    context = _build_template_context(ledger, chapter_id, iteration)

    it_dir = Path(args.io_dir) / context.chapter_id / f"iter_{context.iteration:02d}" / "out"

    planner_template = {
        "focus_areas": [
            "clarify scope in ## Thesis",
            "add measurable outcomes in ## Concrete Example 1",
            "add operational risk in ## Trade-offs",
        ],
        "structural_changes": [],
        "risk_flags": ["possible repetition with Chapter 02"],
        "target_word_delta": "+200",
    }
    critic_template = {
        "structure_score": 0.0,
        "clarity_score": 0.0,
        "example_density": 0.0,
        "tradeoff_presence": False,
        "failure_modes_present": False,
        "drift_score": 0.0,
        "violations": ["TEMPLATE: replace with concrete violations"],
        "decision": "refine",
    }

    created = []
    if _write_if_missing(it_dir / "planner.json", json.dumps(planner_template, indent=2, sort_keys=True) + "\n", force=args.force):
        created.append("planner.json")
    if _write_if_missing(it_dir / "critic.json", json.dumps(critic_template, indent=2, sort_keys=True) + "\n", force=args.force):
        created.append("critic.json")
    if _write_if_missing(it_dir / "writer.md", context.chapter_text, force=args.force):
        created.append("writer.md")

    if created:
        sys.stdout.write(str(it_dir.relative_to(REPO_ROOT)) + ": created " + ", ".join(created) + "\n")
    else:
        sys.stdout.write(str(it_dir.relative_to(REPO_ROOT)) + ": nothing to do (files exist; use --force to overwrite)\n")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TemplateError as exc:
        sys.stderr.write(f"TemplateError: {exc}\n")
        raise SystemExit(2)
