# Plan

1. Add a deterministic `force-stop-close-idempotency` mode in `state/copilot_sdk_smoke_test.py`.
2. Wire the new mode into usage text, parser choices, and mode dispatch.
3. Run deterministic non-live smoke modes to verify no regressions.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_039/01-task.md`
- `state/migration_iterations/iter_039/02-plan.md`
- `state/migration_iterations/iter_039/03-execution.md`
- `state/migration_iterations/iter_039/04-validation.md`
- `state/migration_iterations/iter_039/05-risks-and-decisions.md`
- `state/migration_iterations/iter_039/06-next-iteration.md`
- `state/migration_iterations/iter_039/07-summary.md`
