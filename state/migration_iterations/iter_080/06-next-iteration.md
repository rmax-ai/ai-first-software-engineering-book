# Next Iteration

## Recommended next task
Normalize the remaining fallback-error snippet mention in `state/migration_iterations/iter_079/01-task.md` acceptance criteria so it uses `uv run python` wording.

## Why it is next
This is the next adjacent one-line cleanup in the same command-text normalization stream and keeps migration history consistent.

## Concrete acceptance criteria
- `git --no-pager show HEAD:state/migration_iterations/iter_079/01-task.md | rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`'` confirms pre-edit legacy wording.
- Replace that snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_079/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_079/01-task.md`
- `state/migration_iterations/iter_081/*.md`
