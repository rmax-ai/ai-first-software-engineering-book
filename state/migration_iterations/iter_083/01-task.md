# Task

## Selected task title
Normalize the remaining escaped fallback-error snippet wording in `state/migration_iterations/iter_081/01-task.md` acceptance criteria to use `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_082/06-next-iteration.md` marked this exact one-line normalization as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `git --no-pager show HEAD^:state/migration_iterations/iter_081/01-task.md | rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`'` confirms pre-edit legacy escaped wording.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_081/01-task.md` evidence.
