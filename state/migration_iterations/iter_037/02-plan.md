# Plan

1. Update `state/copilot_sdk_smoke_test.py` with a new deterministic mode that patches `session.destroy()` to fail, checks first `close()` error detail, then calls `close()` again.
2. Wire the new mode through CLI docs, mode choices, help text, and dispatch.
3. Run deterministic smoke modes to confirm existing paths and the new path pass.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_037/01-task.md`
- `state/migration_iterations/iter_037/02-plan.md`
- `state/migration_iterations/iter_037/03-execution.md`
- `state/migration_iterations/iter_037/04-validation.md`
- `state/migration_iterations/iter_037/05-risks-and-decisions.md`
- `state/migration_iterations/iter_037/06-next-iteration.md`
- `state/migration_iterations/iter_037/07-summary.md`
