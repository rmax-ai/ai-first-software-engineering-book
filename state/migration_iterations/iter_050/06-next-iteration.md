# Next Iteration

## Recommended next task
Backfill the next contiguous older batch (`iter_022`-`iter_023`) to replace bare smoke-test `python` snippets with `uv run python` in `03-execution.md` and `04-validation.md`.

## Why it is next
This continues the same normalization pattern in adjacent historical artifacts that still contain outdated command style.

## Concrete acceptance criteria
- Update smoke-test command snippets in `iter_022` and `iter_023` `03-execution.md`/`04-validation.md` from `python ...` to `uv run python ...`.
- Keep non-command narrative unchanged.
- Capture targeted diff/search evidence for the touched files.

## Expected files to touch
- `state/migration_iterations/iter_022/03-execution.md`
- `state/migration_iterations/iter_022/04-validation.md`
- `state/migration_iterations/iter_023/03-execution.md`
- `state/migration_iterations/iter_023/04-validation.md`
