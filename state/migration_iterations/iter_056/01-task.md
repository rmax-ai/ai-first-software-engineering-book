# Task

## Selected task title
Backfill `state/migration_iterations/iter_022/01-task.md` to normalize the remaining fallback-error smoke command snippet.

## Why this task now
`iter_055/06-next-iteration.md` explicitly handed off this single-file command normalization as the smallest unfinished migration cleanup.

## Acceptance criteria for this iteration
- Replace `python state/copilot_sdk_smoke_test.py --mode fallback-error` with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` in `state/migration_iterations/iter_022/01-task.md`.
- Keep all non-command text unchanged.
- Capture targeted search/diff evidence for the file.
