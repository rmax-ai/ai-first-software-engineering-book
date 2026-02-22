#!/usr/bin/env python3
"""File-backed storage for large ledger iteration logs."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_ROOT = REPO_ROOT / "state" / "ledger"
REPO_LOG_DIR = LEDGER_ROOT / "repo_iteration_log"
CHAPTER_LOG_DIR = LEDGER_ROOT / "iteration_log"


def _utc_now_iso() -> str:
    return dt.datetime.now(tz=dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _normalize_timestamp_for_filename(timestamp: str | None) -> str:
    raw = (timestamp or "").strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    parsed: dt.datetime | None = None
    if raw:
        try:
            parsed = dt.datetime.fromisoformat(raw)
        except ValueError:
            parsed = None
    if parsed is None:
        parsed = dt.datetime.now(tz=dt.timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    text = parsed.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return text.replace(":", "-")


def _safe_token(value: str) -> str:
    token = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip())
    return token.strip("-._") or "unknown"


def _to_repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _unique_path(base_dir: Path, stem: str) -> Path:
    candidate = base_dir / f"{stem}.json"
    suffix = 2
    while candidate.exists():
        candidate = base_dir / f"{stem}__{suffix:02d}.json"
        suffix += 1
    return candidate


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(path)


def append_repo_iteration_entry(entry: dict[str, Any]) -> str:
    timestamp = _normalize_timestamp_for_filename(str(entry.get("timestamp") or _utc_now_iso()))
    try:
        iteration = int(entry.get("iteration", 0) or 0)
    except (TypeError, ValueError):
        iteration = 0
    stem = f"{timestamp}__iter-{iteration:06d}"
    path = _unique_path(REPO_LOG_DIR, stem)
    _write_json_atomic(path, entry)
    return _to_repo_relative(path)


def append_chapter_iteration_entry(chapter_id: str, entry: dict[str, Any]) -> str:
    timestamp = _normalize_timestamp_for_filename(str(entry.get("timestamp") or _utc_now_iso()))
    chapter_token = _safe_token(chapter_id)
    try:
        iteration = int(entry.get("iteration", 0) or 0)
    except (TypeError, ValueError):
        iteration = 0
    stem = f"{timestamp}__chapter-{chapter_token}__iter-{iteration:06d}"
    path = _unique_path(CHAPTER_LOG_DIR, stem)
    _write_json_atomic(path, entry)
    return _to_repo_relative(path)


def _dedupe_paths(paths: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        ordered.append(path)
    return ordered


def load_entries_from_relative_paths(paths: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    entries: list[dict[str, Any]] = []
    errors: list[str] = []
    for rel_path in paths:
        rel = str(rel_path or "").strip()
        if not rel:
            errors.append("Log path entries must be non-empty strings")
            continue
        path = REPO_ROOT / rel
        if not path.exists():
            errors.append(f"Missing log file: {rel}")
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            loaded = json.loads(raw)
        except Exception as exc:
            errors.append(f"Invalid log JSON at {rel}: {exc}")
            continue
        if not isinstance(loaded, dict):
            errors.append(f"Log file must contain a JSON object: {rel}")
            continue
        entries.append(loaded)
    return entries, errors


def compact_ledger_logs(ledger: dict[str, Any], tail_size: int = 50) -> dict[str, int]:
    stats = {
        "repo_entries_migrated": 0,
        "chapter_entries_migrated": 0,
        "repo_files_written": 0,
        "chapter_files_written": 0,
    }

    repo_paths = [str(p) for p in ledger.get("repo_iteration_log_files", []) if isinstance(p, str)]
    repo_inline = ledger.get("repo_iteration_log")
    if isinstance(repo_inline, list):
        for entry in repo_inline:
            if not isinstance(entry, dict):
                continue
            rel_path = append_repo_iteration_entry(entry)
            repo_paths.append(rel_path)
            stats["repo_entries_migrated"] += 1
            stats["repo_files_written"] += 1

    repo_tail = [entry for entry in (repo_inline or []) if isinstance(entry, dict)][-tail_size:]
    ledger["repo_iteration_log_files"] = _dedupe_paths(repo_paths)
    ledger["repo_iteration_log_tail"] = repo_tail
    ledger["repo_iteration_log"] = []

    try:
        max_repo_iter = max((int(entry.get("iteration", 0) or 0) for entry in repo_tail), default=0)
    except Exception:
        max_repo_iter = 0
    current_counter = int(ledger.get("repo_iteration_counter", 0) or 0)
    ledger["repo_iteration_counter"] = max(current_counter, max_repo_iter)

    chapters = ledger.get("chapters")
    if isinstance(chapters, dict):
        for chapter_id, chapter in chapters.items():
            if not isinstance(chapter, dict):
                continue
            chapter_paths = [str(p) for p in chapter.get("iteration_log_files", []) if isinstance(p, str)]
            chapter_inline = chapter.get("iteration_log")
            if isinstance(chapter_inline, list):
                for entry in chapter_inline:
                    if not isinstance(entry, dict):
                        continue
                    rel_path = append_chapter_iteration_entry(chapter_id, entry)
                    chapter_paths.append(rel_path)
                    stats["chapter_entries_migrated"] += 1
                    stats["chapter_files_written"] += 1
            chapter_tail = [entry for entry in (chapter_inline or []) if isinstance(entry, dict)][-tail_size:]
            chapter["iteration_log_files"] = _dedupe_paths(chapter_paths)
            chapter["iteration_log_tail"] = chapter_tail
            chapter["iteration_log"] = []

    return stats
