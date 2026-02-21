# Task

## Selected task title
Backfill `state/migration_iterations/iter_046/01-task.md` to normalize the remaining live smoke-test command snippet.

## Why this task now
`state/migration_iterations/iter_057/06-next-iteration.md` identified this one-line normalization as the smallest unfinished migration cleanup task.

## Acceptance criteria for this iteration
- Replace `python state/copilot_sdk_smoke_test.py --mode live` with `uv run python state/copilot_sdk_smoke_test.py --mode live` in `state/migration_iterations/iter_046/01-task.md`.
- Keep all non-command narrative text unchanged.
- Capture targeted command-search and diff/show evidence for only that file.
