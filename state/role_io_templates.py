#!/usr/bin/env python3
"""Generate role I/O templates for the Planner/Writer/Critic loop.

This is intentionally minimal and deterministic. It does not run the kernel.
It only creates scaffold files under `state/role_io/<chapter-id>/iter_XX/out/`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "state" / "ledger.json"


class TemplateError(RuntimeError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise TemplateError(f"Missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise TemplateError(f"Invalid JSON: {path}: {exc}") from exc


def _write_if_missing(path: Path, content: str, *, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _resolve_iteration(ledger: dict[str, Any], chapter_id: str, iteration: int | None) -> int:
    chapters = ledger.get("chapters")
    if not isinstance(chapters, dict) or chapter_id not in chapters or not isinstance(chapters[chapter_id], dict):
        raise TemplateError(f"Unknown chapter_id: {chapter_id}")
    meta: dict[str, Any] = chapters[chapter_id]

    if iteration is not None:
        if iteration <= 0:
            raise TemplateError("--iteration must be positive")
        return iteration

    current_iteration_raw = meta.get("current_iteration", 0)
    try:
        current_iteration = int(current_iteration_raw)
    except (TypeError, ValueError):
        current_iteration = 0
    return current_iteration + 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="role-io-templates", description="Generate Planner/Writer/Critic template outputs")
    parser.add_argument("--chapter-id", required=True)
    parser.add_argument("--io-dir", type=Path, default=REPO_ROOT / "state" / "role_io")
    parser.add_argument("--iteration", type=int, default=None, help="Iteration number to scaffold (defaults to current_iteration+1)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")

    args = parser.parse_args(argv)

    ledger = _load_json(LEDGER_PATH)
    chapter_id = str(args.chapter_id)
    iteration = _resolve_iteration(ledger, chapter_id, args.iteration)

    chapters = ledger["chapters"]
    meta: dict[str, Any] = chapters[chapter_id]
    chapter_path = meta.get("path")
    if not isinstance(chapter_path, str) or not chapter_path:
        raise TemplateError(f"Missing chapters.{chapter_id}.path")

    chapter_file = REPO_ROOT / chapter_path
    try:
        chapter_text = chapter_file.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise TemplateError(f"Chapter file not found: {chapter_file}") from exc

    it_dir = Path(args.io_dir) / chapter_id / f"iter_{iteration:02d}" / "out"

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
    if _write_if_missing(it_dir / "writer.md", chapter_text, force=args.force):
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
