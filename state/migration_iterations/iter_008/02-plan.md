# Plan

1. Update `state/llm_client.py` to clear `_sdk_client` on successful `stop()` and `force_stop()` paths while preserving current error mapping.
2. Run targeted syntax validation for `state/llm_client.py`.
3. Run focused behavioral checks for reference reset and error-path messaging.
4. Record execution, validation, risks, and next task recommendation in iteration artifacts.

## Files expected to change
- `state/llm_client.py`
- `state/migration_iterations/iter_008/01-task.md`
- `state/migration_iterations/iter_008/02-plan.md`
- `state/migration_iterations/iter_008/03-execution.md`
- `state/migration_iterations/iter_008/04-validation.md`
- `state/migration_iterations/iter_008/05-risks-and-decisions.md`
- `state/migration_iterations/iter_008/06-next-iteration.md`
- `state/migration_iterations/iter_008/07-summary.md`
