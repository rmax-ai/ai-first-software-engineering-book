# Next Iteration

## Recommended next task
Normalize the remaining bare snippet mention in `state/migration_iterations/iter_064/06-next-iteration.md` acceptance criteria to use `uv run python` wording.

## Why it is next
It is an adjacent migration handoff artifact and can be corrected with a single-line, low-risk edit.

## Concrete acceptance criteria
- `rg -n '\`python state/copilot_sdk_smoke_test.py --mode fallback-timeout\`' state/migration_iterations/iter_064/06-next-iteration.md` confirms the legacy mention before edit.
- Replace that snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout`.
- Capture targeted `rg` plus `git --no-pager diff -- state/migration_iterations/iter_064/06-next-iteration.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_064/06-next-iteration.md`
- `state/migration_iterations/iter_068/*.md`
