# Next Iteration

## Recommended next task
Backfill one older contiguous batch of historical iteration artifacts (e.g., iter_039–iter_043) to replace bare smoke-test `python` snippets with `uv run python`.

## Why it is next
Recent artifacts are now normalized, but adjacent older iterations still contain outdated command style that can be copied forward.

## Concrete acceptance criteria
- Update `03-execution.md` and `04-validation.md` command snippets in the chosen older batch from bare `python ...` to `uv run python ...`.
- Keep all non-command narrative unchanged.
- Spot-check at least one updated file with diff/search evidence.

## Expected files to touch
- `state/migration_iterations/iter_03X/03-execution.md`
- `state/migration_iterations/iter_03X/04-validation.md`
- `state/migration_iterations/iter_04X/03-execution.md`
- `state/migration_iterations/iter_04X/04-validation.md`
