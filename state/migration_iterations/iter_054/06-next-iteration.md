# Next Iteration

## Recommended next task
Backfill `iter_026` handoff artifacts to replace bare smoke-test `python` snippets with `uv run python`.

## Why it is next
After normalizing `iter_026` execution/validation docs in this iteration, the smallest adjacent unfinished normalization scope is the same iteration's handoff docs (`01-task.md` and `06-next-iteration.md`), each still containing bare smoke-test command snippets.

## Concrete acceptance criteria
- Update smoke-test command snippets in `state/migration_iterations/iter_026/01-task.md` and `state/migration_iterations/iter_026/06-next-iteration.md` from `python ...` to `uv run python ...`.
- Keep non-command narrative unchanged.
- Capture targeted diff/search evidence for the touched files.

## Expected files to touch
- `state/migration_iterations/iter_026/01-task.md`
- `state/migration_iterations/iter_026/06-next-iteration.md`
