# Next Iteration

## Recommended next task
Normalize the legacy snippet text in `state/migration_iterations/iter_065/06-next-iteration.md` so it no longer references bare `python state/copilot_sdk_smoke_test.py --mode fallback-error`.

## Why it is next
It is the nearest adjacent handoff artifact still carrying a bare command reference and can be fixed with a single-line, low-risk edit.

## Concrete acceptance criteria
- `rg -n 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_065/06-next-iteration.md` confirms the legacy reference before edit.
- Replace the bare snippet reference with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` plus `git --no-pager diff -- state/migration_iterations/iter_065/06-next-iteration.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_065/06-next-iteration.md`
- `state/migration_iterations/iter_067/*.md`
