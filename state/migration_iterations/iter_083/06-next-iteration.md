# Next Iteration

## Recommended next task
Normalize the escaped fallback-error snippet wording in `state/migration_iterations/iter_082/01-task.md` so it uses `uv run python` in the acceptance-criteria evidence note.

## Why it is next
This is the next adjacent one-line normalization in the same migration-artifact wording cleanup stream.

## Concrete acceptance criteria
- `rg -nF 'uv run python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_082/01-task.md` confirms the remaining legacy snippet mention.
- Replace that escaped snippet mention so it uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_082/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_082/01-task.md`
- `state/migration_iterations/iter_084/*.md`
