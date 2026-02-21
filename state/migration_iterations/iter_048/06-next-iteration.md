# Next Iteration

## Recommended next task
Backfill the most recent migration iteration artifacts (latest 5–10 iterations) to use `uv run python state/copilot_sdk_smoke_test.py ...` in validation/execution snippets.

## Why it is next
Active guidance is now fixed, but recent historical artifacts still repeat old command patterns that can be copied forward.

## Concrete acceptance criteria
- Update command snippets in the selected recent iteration markdown files from bare `python ...` to `uv run python ...`.
- Keep all non-command narrative unchanged.
- Spot-check one updated iteration file for correctness after edits.

## Expected files to touch
- `state/migration_iterations/iter_0XX/03-execution.md` (recent iterations only)
- `state/migration_iterations/iter_0XX/04-validation.md` (recent iterations only)
