# Next Iteration

## Recommended next task
Normalize the remaining bare snippet mention in `state/migration_iterations/iter_066/04-validation.md` command 1 to use `uv run python` wording.

## Why it is next
This is another adjacent migration handoff artifact cleanup that can be completed as a low-risk, single-line documentation fix.

## Concrete acceptance criteria
- `rg -n "\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`" state/migration_iterations/iter_066/04-validation.md` confirms the normalized mention before edit.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` plus `git --no-pager diff -- state/migration_iterations/iter_066/04-validation.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_066/04-validation.md`
- `state/migration_iterations/iter_069/*.md`
