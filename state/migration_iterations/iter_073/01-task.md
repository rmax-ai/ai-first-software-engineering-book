# Task

## Selected task title
Normalize the remaining bare fallback-error snippet mention in `state/migration_iterations/iter_070/01-task.md` acceptance criteria to use `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_072/06-next-iteration.md` explicitly handed off this exact one-line cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_070/01-task.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention so the line uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_070/01-task.md` evidence.
