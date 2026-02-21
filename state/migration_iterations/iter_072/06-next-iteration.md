# Next Iteration

## Recommended next task
Normalize the remaining bare fallback-error snippet mention in `state/migration_iterations/iter_070/01-task.md` acceptance criteria to use `uv run python` wording.

## Why it is next
This is another adjacent one-line artifact cleanup in the same normalization stream and can be verified quickly with focused checks.

## Concrete acceptance criteria
- `rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_070/01-task.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_070/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_070/01-task.md`
- `state/migration_iterations/iter_073/*.md`
