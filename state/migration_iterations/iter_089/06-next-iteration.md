# Next Iteration

## Recommended next task
Normalize the remaining legacy fallback-error snippet wording in `state/migration_iterations/iter_082/01-task.md` to use `uv run python` in the acceptance-criteria evidence note.

## Why it is next
This is the next adjacent one-line cleanup in the same migration-artifact wording stream and preserves incremental iteration scope.

## Concrete acceptance criteria
- `rg -nF 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_082/01-task.md` confirms the legacy snippet mention.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_082/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_082/01-task.md`
- `state/migration_iterations/iter_090/*.md`
