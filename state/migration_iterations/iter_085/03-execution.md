# Execution

## Commands/tools run
- `rg -nF "python state/copilot_sdk_smoke_test.py --mode fallback-error" state/migration_iterations/iter_083/01-task.md`
- `apply_patch` on `state/migration_iterations/iter_083/01-task.md` to change one acceptance-criteria line.
- `git --no-pager diff -- state/migration_iterations/iter_083/01-task.md`
- `rg -nF "uv run python state/copilot_sdk_smoke_test.py --mode fallback-error" state/migration_iterations/iter_083/01-task.md`
- `git add state/migration_iterations/iter_083/01-task.md && git commit -m "Normalize fallback-error snippet wording"`

## Files changed
- `state/migration_iterations/iter_083/01-task.md`

## Short rationale per change
- Replaced the remaining escaped fallback-error snippet mention with normalized `uv run python` wording to keep migration artifacts consistent with repository command conventions.
