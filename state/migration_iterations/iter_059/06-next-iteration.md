# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_046/07-summary.md` to replace the remaining bare live smoke-test command snippet with `uv run python`.

## Why it is next
This is the next smallest adjacent normalization in the same historical iteration and keeps cleanup incremental with minimal risk.

## Concrete acceptance criteria
- Update `state/migration_iterations/iter_046/07-summary.md` by changing `python state/copilot_sdk_smoke_test.py --mode live` to `uv run python state/copilot_sdk_smoke_test.py --mode live`.
- Keep all non-command narrative text unchanged.
- Capture targeted search and diff evidence for only that file.

## Expected files to touch
- `state/migration_iterations/iter_046/07-summary.md`
