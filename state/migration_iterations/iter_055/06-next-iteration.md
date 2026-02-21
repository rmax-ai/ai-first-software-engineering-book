# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_022/01-task.md` to replace the remaining bare smoke-test command snippet with `uv run python`.

## Why it is next
After finishing all remaining `iter_026` normalization from the prior handoff, the smallest unfinished adjacent cleanup is a single-file acceptance-criteria command snippet in `iter_022/01-task.md`.

## Concrete acceptance criteria
- Change `python state/copilot_sdk_smoke_test.py --mode fallback-error` to `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` in `state/migration_iterations/iter_022/01-task.md`.
- Keep all non-command text unchanged.
- Capture targeted diff/search evidence for that file.

## Expected files to touch
- `state/migration_iterations/iter_022/01-task.md`
