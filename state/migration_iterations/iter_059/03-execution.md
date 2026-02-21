# Execution

## Commands/tools run
- `view prompts/migration-iteration/execute.md`
- `view state/copilot-sdk-migration-plan.md`
- `view state/migration_iterations/iter_058/06-next-iteration.md`
- `apply_patch` on `state/migration_iterations/iter_046/02-plan.md`
- `rg -n "python state/copilot_sdk_smoke_test.py --mode live|uv run python state/copilot_sdk_smoke_test.py --mode live" state/migration_iterations/iter_046/02-plan.md`
- `git --no-pager diff -- state/migration_iterations/iter_046/02-plan.md`

## Files changed
- `state/migration_iterations/iter_046/02-plan.md`

## Short rationale per change
- Normalized the remaining bare live smoke-test command snippet to `uv run python` to match migration command conventions.
