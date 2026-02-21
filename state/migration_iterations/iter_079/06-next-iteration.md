# Next Iteration

## Recommended next task
Normalize the remaining escaped bare fallback-error snippet mention in `state/migration_iterations/iter_078/01-task.md` acceptance criteria to use `uv run python` wording.

## Why it is next
This is the nearest remaining one-line cleanup in the same command-text normalization chain and keeps the migration history consistent.

## Concrete acceptance criteria
- `git --no-pager show HEAD:state/migration_iterations/iter_078/01-task.md | rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`'` confirms pre-edit legacy wording.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_078/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_078/01-task.md`
- `state/migration_iterations/iter_080/*.md`
