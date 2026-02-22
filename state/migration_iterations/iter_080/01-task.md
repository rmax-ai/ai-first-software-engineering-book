# Task

## Selected task title
Normalize the remaining escaped bare fallback-error snippet mention in `state/migration_iterations/iter_078/01-task.md` acceptance criteria to use `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_079/06-next-iteration.md` designated this exact one-line normalization as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `git --no-pager show HEAD:state/migration_iterations/iter_078/01-task.md | rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`'` confirms the normalized snippet mention.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_078/01-task.md` evidence.
