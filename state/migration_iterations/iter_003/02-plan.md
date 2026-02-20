# Plan

1. Update `state/llm_client.py` to route non-mock calls through a guarded SDK helper.
2. Keep existing provider-specific HTTP methods as fallback paths.
3. Preserve `mock` provider path exactly.
4. Run targeted syntax validation for touched modules.

## Expected files to change
- `state/llm_client.py`
- `state/migration_iterations/iter_003/01-task.md`
- `state/migration_iterations/iter_003/02-plan.md`
- `state/migration_iterations/iter_003/03-execution.md`
- `state/migration_iterations/iter_003/04-validation.md`
- `state/migration_iterations/iter_003/05-risks-and-decisions.md`
- `state/migration_iterations/iter_003/06-next-iteration.md`
- `state/migration_iterations/iter_003/07-summary.md`
