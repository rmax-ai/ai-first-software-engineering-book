# Next Iteration

## Recommended next task
Normalize the remaining escaped bare fallback-error snippet mention in `state/migration_iterations/iter_077/01-task.md` acceptance criteria to use `uv run python` wording.

## Why it is next
This is the nearest remaining instance in the same minimal historical command-text normalization stream.

## Concrete acceptance criteria
- `rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_077/01-task.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention so the acceptance-criteria line uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_077/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_077/01-task.md`
- `state/migration_iterations/iter_079/*.md`
