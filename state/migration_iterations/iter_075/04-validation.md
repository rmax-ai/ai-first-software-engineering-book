# Validation

## Verification commands run
- `rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-timeout\`' state/migration_iterations/iter_071/01-task.md || true`
- `rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout\`' state/migration_iterations/iter_071/01-task.md`
- `git --no-pager diff -- state/migration_iterations/iter_071/01-task.md`

## Observed outputs/results
- Post-edit, no backticked bare fallback-timeout snippet remains in `state/migration_iterations/iter_071/01-task.md`.
- The acceptance-criteria line now contains `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout` wording.
- Scoped diff shows exactly one changed line in the targeted file.

## Pass/fail against acceptance criteria
- Pass: legacy snippet mention was identified and normalized.
- Pass: change scope remained a single targeted line.
- Pass: targeted checks and scoped diff evidence were captured.
