# Next Iteration

## Recommended next task
Normalize the remaining bare fallback-error snippet mention in `state/migration_iterations/iter_067/04-validation.md` command 1 to use `uv run python` wording.

## Why it is next
This is the nearest adjacent one-line cleanup in the same migration-artifact chain and can be completed with low risk and clear validation evidence.

## Concrete acceptance criteria
- `rg -n '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_067/04-validation.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_067/04-validation.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_067/04-validation.md`
- `state/migration_iterations/iter_070/*.md`
