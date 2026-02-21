# Next Iteration

## Recommended next task
Backfill `state/migration_iterations/iter_046/06-next-iteration.md` to replace the remaining bare import-check command snippet with `uv run python`.

## Why it is next
It is the next smallest adjacent normalization in the same file and continues the low-risk one-line cleanup pattern.

## Concrete acceptance criteria
- Update `state/migration_iterations/iter_046/06-next-iteration.md` by changing `python -c "import copilot"` to `uv run python -c "import copilot"`.
- Keep all non-command narrative text unchanged.
- Capture targeted search and diff evidence for only that file.

## Expected files to touch
- `state/migration_iterations/iter_046/06-next-iteration.md`
