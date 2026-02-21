# Next Iteration

## Recommended next task
Normalize the next remaining direct legacy snippet in `state/migration_iterations/iter_024/07-summary.md` from bare `python` to `uv run python`.

## Why it is next
After updating the highest-priority remaining snippet in `iter_045`, the next direct command snippet still in bare form is in `iter_024/07-summary.md`.

## Concrete acceptance criteria
- `rg -n "\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout\`" state/migration_iterations/iter_024/07-summary.md` finds the normalized snippet wording.
- Update that snippet to `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout`.
- Capture `rg` and `git --no-pager diff -- state/migration_iterations/iter_024/07-summary.md` evidence in the new iteration artifacts.

## Expected files to touch
- `state/migration_iterations/iter_024/07-summary.md`
- `state/migration_iterations/iter_0XX/*.md` (new iteration handoff artifacts)
