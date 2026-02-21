# Task

## Selected task title
Backfill `state/migration_iterations/iter_046/02-plan.md` to normalize the remaining live smoke-test command snippet.

## Why this task now
`state/migration_iterations/iter_058/06-next-iteration.md` explicitly recommended this one-line command normalization as the smallest unfinished migration task.

## Acceptance criteria for this iteration
- Replace `python state/copilot_sdk_smoke_test.py --mode live` with `uv run python state/copilot_sdk_smoke_test.py --mode live` in `state/migration_iterations/iter_046/02-plan.md`.
- Keep all non-command narrative text unchanged.
- Capture targeted search and diff evidence for only that file.
