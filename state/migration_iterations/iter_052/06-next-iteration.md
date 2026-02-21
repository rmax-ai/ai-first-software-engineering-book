# Next Iteration

## Recommended next task
Backfill the next contiguous older batch (`iter_018`-`iter_019`) to replace bare smoke-test `python` snippets with `uv run python` in `03-execution.md` and `04-validation.md`.

## Why it is next
It continues the same minimal historical normalization pattern in immediately adjacent older artifacts that still use outdated command snippets.

## Concrete acceptance criteria
- Update smoke-test command snippets in `iter_018` and `iter_019` `03-execution.md`/`04-validation.md` from `python ...` to `uv run python ...`.
- Keep non-command narrative unchanged.
- Capture targeted diff/search evidence for the touched files.

## Expected files to touch
- `state/migration_iterations/iter_018/03-execution.md`
- `state/migration_iterations/iter_018/04-validation.md`
- `state/migration_iterations/iter_019/03-execution.md`
- `state/migration_iterations/iter_019/04-validation.md`
