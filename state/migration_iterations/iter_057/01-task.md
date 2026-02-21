# Task

## Selected task title
Backfill `state/migration_iterations/iter_021/06-next-iteration.md` to normalize the remaining fallback-error smoke command snippet.

## Why this task now
`state/migration_iterations/iter_056/06-next-iteration.md` explicitly handed off this one-line normalization as the smallest unfinished migration task.

## Acceptance criteria for this iteration
- Replace `python state/copilot_sdk_smoke_test.py --mode fallback-error` with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` in `state/migration_iterations/iter_021/06-next-iteration.md`.
- Keep all non-command narrative text unchanged.
- Capture targeted `rg` and diff evidence for the file.
