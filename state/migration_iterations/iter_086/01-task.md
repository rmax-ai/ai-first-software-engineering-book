# Task

## Selected task title
Normalize the escaped fallback-error snippet wording in `state/migration_iterations/iter_083/03-execution.md` so it uses escaped `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_085/06-next-iteration.md` identified this as the next smallest unfinished one-line normalization.

## Acceptance criteria for this iteration
- `rg -nF "\\`python state/copilot_sdk_smoke_test.py --mode fallback-error\\`" state/migration_iterations/iter_083/03-execution.md` confirms the legacy escaped snippet mention.
- Replace that escaped snippet mention with `\\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\\`` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/03-execution.md` evidence.
