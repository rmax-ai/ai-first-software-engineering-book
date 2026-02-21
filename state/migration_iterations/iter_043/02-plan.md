# Plan

1. Add a new smoke-test mode in `state/copilot_sdk_smoke_test.py` for stop-failure + destroy-unavailable close idempotency.
2. Wire the mode into CLI usage text, argument choices, help text, and dispatch.
3. Run targeted validation commands for the new mode and existing deterministic baseline.
4. Record outcomes and produce next iteration recommendation.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_043/01-task.md`
- `state/migration_iterations/iter_043/02-plan.md`
- `state/migration_iterations/iter_043/03-execution.md`
- `state/migration_iterations/iter_043/04-validation.md`
- `state/migration_iterations/iter_043/05-risks-and-decisions.md`
- `state/migration_iterations/iter_043/06-next-iteration.md`
- `state/migration_iterations/iter_043/07-summary.md`
