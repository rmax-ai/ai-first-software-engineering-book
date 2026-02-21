# Next Iteration

## Recommended next task
Normalize the remaining bare fallback-error snippet mention in `state/migration_iterations/iter_068/06-next-iteration.md` acceptance criteria to use `uv run python` wording.

## Why it is next
This is the nearest adjacent one-line artifact cleanup in the same normalization chain and can be validated quickly with focused evidence.

## Concrete acceptance criteria
- `rg -n '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_068/06-next-iteration.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_068/06-next-iteration.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_068/06-next-iteration.md`
- `state/migration_iterations/iter_072/*.md`
