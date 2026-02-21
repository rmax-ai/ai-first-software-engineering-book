# Plan

1. Add one new deterministic smoke mode for combined `stop()` + `session.destroy()` failures with close idempotency assertions.
2. Wire the mode into usage docs, argparse choices/help, and mode dispatch in `state/copilot_sdk_smoke_test.py`.
3. Run the new mode plus the deterministic non-live mode matrix.
4. Record evidence and write the iteration handoff artifacts.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_044/01-task.md`
- `state/migration_iterations/iter_044/02-plan.md`
- `state/migration_iterations/iter_044/03-execution.md`
- `state/migration_iterations/iter_044/04-validation.md`
- `state/migration_iterations/iter_044/05-risks-and-decisions.md`
- `state/migration_iterations/iter_044/06-next-iteration.md`
- `state/migration_iterations/iter_044/07-summary.md`
