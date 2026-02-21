# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_046/06-next-iteration.md` to replace the remaining bare live smoke-test command snippet with `uv run python`.

## Why it is next
It is the next smallest adjacent historical normalization in the same iteration and continues the low-risk cleanup pattern.

## Concrete acceptance criteria
- Update `state/migration_iterations/iter_046/06-next-iteration.md` by changing `python state/copilot_sdk_smoke_test.py --mode live` to `uv run python state/copilot_sdk_smoke_test.py --mode live`.
- Keep all non-command narrative text unchanged.
- Capture targeted search and diff evidence for only that file.

## Expected files to touch
- `state/migration_iterations/iter_046/06-next-iteration.md`
