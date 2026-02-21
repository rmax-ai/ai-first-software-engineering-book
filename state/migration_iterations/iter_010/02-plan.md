# Plan

1. Execute focused Python validation script against `state.llm_client.LLMClient`.
2. Assert missing API key and connection failure paths produce actionable `LLMClientError` messages.
3. Assert `mock` planner/critic outputs remain deterministic.
4. Record results and recommend one next task.

## Files expected to change
- `state/migration_iterations/iter_010/01-task.md`
- `state/migration_iterations/iter_010/02-plan.md`
- `state/migration_iterations/iter_010/03-execution.md`
- `state/migration_iterations/iter_010/04-validation.md`
- `state/migration_iterations/iter_010/05-risks-and-decisions.md`
- `state/migration_iterations/iter_010/06-next-iteration.md`
- `state/migration_iterations/iter_010/07-summary.md`
