# Plan

1. Add a new deterministic smoke mode for stop-unavailable close idempotency.
2. Wire the mode into CLI usage text, parser choices, and dispatch.
3. Run deterministic non-live smoke modes to verify no regressions.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_038/01-task.md`
- `state/migration_iterations/iter_038/02-plan.md`
- `state/migration_iterations/iter_038/03-execution.md`
- `state/migration_iterations/iter_038/04-validation.md`
- `state/migration_iterations/iter_038/05-risks-and-decisions.md`
- `state/migration_iterations/iter_038/06-next-iteration.md`
- `state/migration_iterations/iter_038/07-summary.md`
