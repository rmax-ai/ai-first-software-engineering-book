#!/usr/bin/env python3
"""Migrate legacy state/metrics.json into archive files + latest-only snapshot.

Legacy format (pre-2026-02-23):
  {"chapters": {"<chapter>": {"history": [<entry>, ...]}}}

New format:
  - Per-day archives:
      state/metrics/<chapter>/<YYYY-MM-DD>.json
      {"chapter_id": "...", "date": "YYYY-MM-DD", "history": [<entry>, ...]}
  - Latest-only snapshot:
      state/metrics.json
      {"chapters": {"<chapter>": {"latest": <entry>}}, "generated_at": "..."}

This script is intended for one-time migration of existing repo state.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def _utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _date_from_timestamp(entry: dict[str, Any]) -> str:
    ts = entry.get("timestamp")
    if isinstance(ts, str) and "T" in ts:
        return ts.split("T", 1)[0]
    return "unknown"


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def migrate(*, input_path: Path, archive_root: Path, snapshot_path: Path) -> tuple[int, int, int]:
    raw = _load_json(input_path)
    chapters = raw.get("chapters") if isinstance(raw, dict) else None
    if not isinstance(chapters, dict):
        chapters = {}

    archive_root.mkdir(parents=True, exist_ok=True)

    archive_files_written = 0
    entries_archived = 0
    chapters_with_latest = 0

    snapshot: dict[str, Any] = {"chapters": {}, "generated_at": _utc_now_iso()}

    for chapter_id, blob in chapters.items():
        if not isinstance(chapter_id, str) or not chapter_id.strip():
            continue
        if not isinstance(blob, dict):
            continue

        history = blob.get("history")
        if not isinstance(history, list) or not history:
            continue

        # Build per-day archives.
        by_date: dict[str, list[dict[str, Any]]] = defaultdict(list)
        normalized_history: list[dict[str, Any]] = []
        for entry in history:
            if not isinstance(entry, dict):
                continue
            normalized_history.append(entry)
            by_date[_date_from_timestamp(entry)].append(entry)

        if not normalized_history:
            continue

        for date, entries in sorted(by_date.items(), key=lambda kv: kv[0]):
            archive_path = archive_root / chapter_id / f"{date}.json"
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            archive_payload = {"chapter_id": chapter_id, "date": date, "history": entries}
            archive_path.write_text(_dump_json(archive_payload), encoding="utf-8")
            archive_files_written += 1
            entries_archived += len(entries)

        # Latest-only snapshot.
        snapshot["chapters"][chapter_id] = {"latest": normalized_history[-1]}
        chapters_with_latest += 1

    snapshot_path.write_text(_dump_json(snapshot), encoding="utf-8")
    return archive_files_written, entries_archived, chapters_with_latest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="migrate_metrics_to_archive")
    parser.add_argument("--input", type=Path, default=Path("state/metrics.json"))
    parser.add_argument("--archive-root", type=Path, default=Path("state/metrics"))
    parser.add_argument("--snapshot", type=Path, default=Path("state/metrics.json"))
    args = parser.parse_args(argv)

    archive_files_written, entries_archived, chapters_with_latest = migrate(
        input_path=args.input,
        archive_root=args.archive_root,
        snapshot_path=args.snapshot,
    )
    print(
        json.dumps(
            {
                "archive_files_written": archive_files_written,
                "entries_archived": entries_archived,
                "chapters_with_latest": chapters_with_latest,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
