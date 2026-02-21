# Task

## Selected task title
Normalize the remaining escaped fallback-error snippet mention in `state/migration_iterations/iter_080/01-task.md` acceptance criteria so it uses `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_081/06-next-iteration.md` designated this exact one-line command-text normalization as the next smallest unfinished task.

## Acceptance criteria for this iteration
- `git --no-pager show HEAD:state/migration_iterations/iter_080/01-task.md | rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`'` confirms pre-edit legacy wording.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_080/01-task.md` evidence.
