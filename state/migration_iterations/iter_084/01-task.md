# Task

## Selected task title
Normalize the escaped fallback-error snippet wording in `state/migration_iterations/iter_082/01-task.md` so it uses `uv run python` in acceptance criteria.

## Why this task now
`state/migration_iterations/iter_083/06-next-iteration.md` marked this exact one-line wording cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `rg -nF 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_082/01-task.md` finds the legacy snippet mention before edit.
- Replace the escaped snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted checks plus `git --no-pager diff -- state/migration_iterations/iter_082/01-task.md` evidence.
