# Plan

1. Add one deterministic shutdown mode for `stop()` unavailable + `session.destroy()` failure with close idempotency assertions.
2. Wire the mode into usage docs, argparse choices/help text, and mode dispatch in `state/copilot_sdk_smoke_test.py`.
3. Run the new mode plus the deterministic non-live matrix.
4. Record evidence and write the iteration handoff artifacts.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_045/01-task.md`
- `state/migration_iterations/iter_045/02-plan.md`
- `state/migration_iterations/iter_045/03-execution.md`
- `state/migration_iterations/iter_045/04-validation.md`
- `state/migration_iterations/iter_045/05-risks-and-decisions.md`
- `state/migration_iterations/iter_045/06-next-iteration.md`
- `state/migration_iterations/iter_045/07-summary.md`
