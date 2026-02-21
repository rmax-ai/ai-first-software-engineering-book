# Task

## Selected task title
Normalize the remaining escaped fallback-error command snippet mention in `state/migration_iterations/iter_079/01-task.md` acceptance criteria to use `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_080/06-next-iteration.md` designated this exact one-line command-text normalization as the next smallest unfinished task.

## Acceptance criteria for this iteration
- Pre-edit evidence confirms `state/migration_iterations/iter_079/01-task.md` contained escaped `python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_079/01-task.md` evidence.
