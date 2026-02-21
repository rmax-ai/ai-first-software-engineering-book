# Validation

## Verification commands run
- `rg -nF '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_076/01-task.md`
- `rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_076/01-task.md`
- `git --no-pager show -- state/migration_iterations/iter_076/01-task.md`

## Observed outputs/results
- Legacy escaped bare snippet no longer appears in `state/migration_iterations/iter_076/01-task.md`.
- The acceptance-criteria line now includes escaped `uv run python` wording.
- `git show` confirms a single-line replacement in the target file.

## Pass/fail against acceptance criteria
- Pass: acceptance-criteria snippet mention in `state/migration_iterations/iter_076/01-task.md` now uses `uv run python`.
- Pass: targeted checks and scoped git evidence confirm the one-line normalization.
