# Next Iteration

## Recommended next task
Normalize the remaining legacy fallback-error snippet wording in `state/migration_iterations/iter_083/06-next-iteration.md` to use `uv run python` in the acceptance-criteria evidence note.

## Why it is next
This is another single-line historical-artifact cleanup adjacent to the just-verified scope and keeps migration artifact wording consistent.

## Concrete acceptance criteria
- `rg -nF 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_083/06-next-iteration.md` confirms the legacy snippet mention.
- Replace that mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/06-next-iteration.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_083/06-next-iteration.md`
- `state/migration_iterations/iter_089/*.md`
