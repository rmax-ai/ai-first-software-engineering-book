# Plan

1. Add a minimal SDK usage extraction helper in `state/llm_client.py`.
2. Prefer direct usage fields first, then aggregate from `assistant.usage` events.
3. Keep response content normalization and provider routing behavior unchanged.
4. Run targeted compile/smoke checks for the modified surface.

## Expected files to change
- `state/llm_client.py`
- `state/migration_iterations/iter_004/01-task.md`
- `state/migration_iterations/iter_004/02-plan.md`
- `state/migration_iterations/iter_004/03-execution.md`
- `state/migration_iterations/iter_004/04-validation.md`
- `state/migration_iterations/iter_004/05-risks-and-decisions.md`
- `state/migration_iterations/iter_004/06-next-iteration.md`
- `state/migration_iterations/iter_004/07-summary.md`
