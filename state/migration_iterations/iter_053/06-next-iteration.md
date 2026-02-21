# Next Iteration

## Recommended next task
Backfill `iter_026` execution/validation artifacts to replace bare smoke-test `python` snippets with `uv run python`.

## Why it is next
After updating `iter_018` and `iter_019`, the remaining bare smoke-test command snippets in `03-execution.md`/`04-validation.md` are concentrated in `iter_026`, making it the next smallest unfinished normalization task.

## Concrete acceptance criteria
- Update smoke-test command snippets in `state/migration_iterations/iter_026/03-execution.md` and `state/migration_iterations/iter_026/04-validation.md` from `python ...` to `uv run python ...`.
- Keep non-command narrative unchanged.
- Capture targeted diff/search evidence for the touched files.

## Expected files to touch
- `state/migration_iterations/iter_026/03-execution.md`
- `state/migration_iterations/iter_026/04-validation.md`
