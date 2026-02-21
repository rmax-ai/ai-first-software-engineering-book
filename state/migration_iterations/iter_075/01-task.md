# Task

## Selected task title
Normalize the remaining bare fallback-timeout snippet mention in `state/migration_iterations/iter_071/01-task.md` acceptance criteria to `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_074/06-next-iteration.md` guidance targeted the same snippet-normalization stream, and the referenced fallback-error target was already complete/absent.

## Acceptance criteria for this iteration
- `rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-timeout\`' state/migration_iterations/iter_071/01-task.md` confirms the legacy snippet mention before edit.
- Replace that snippet mention so the acceptance-criteria line uses `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_071/01-task.md` evidence.
