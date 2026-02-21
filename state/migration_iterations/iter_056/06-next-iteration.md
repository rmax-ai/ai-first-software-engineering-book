# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_021/06-next-iteration.md` to replace the remaining bare smoke-test command snippet with `uv run python`.

## Why it is next
This continues the same low-risk normalization pattern on an adjacent migration iteration artifact, keeping each batch to one minimal file edit where a bare snippet still exists.

## Concrete acceptance criteria
- Update `state/migration_iterations/iter_021/06-next-iteration.md` by changing `python state/copilot_sdk_smoke_test.py --mode fallback-error` to `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Keep all non-command narrative text unchanged.
- Capture targeted `rg` and diff evidence for only that file.

## Expected files to touch
- `state/migration_iterations/iter_021/06-next-iteration.md`
