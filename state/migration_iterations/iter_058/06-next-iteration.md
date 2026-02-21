# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_046/02-plan.md` to replace the remaining bare live smoke-test command snippet with `uv run python`.

## Why it is next
This is another one-line historical command normalization adjacent to the file updated this iteration, keeping cleanup low-risk and incremental.

## Concrete acceptance criteria
- Update `state/migration_iterations/iter_046/02-plan.md` by changing `python state/copilot_sdk_smoke_test.py --mode live` to `uv run python state/copilot_sdk_smoke_test.py --mode live`.
- Keep all non-command narrative text unchanged.
- Capture targeted search and diff evidence for only that file.

## Expected files to touch
- `state/migration_iterations/iter_046/02-plan.md`
