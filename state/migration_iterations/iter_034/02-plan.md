# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a new `force-stop-unavailable` mode.
2. Implement a deterministic scenario where `stop()` raises and `force_stop` is non-callable.
3. Validate shutdown error message assertions for both `stop()` failure and unavailable `force_stop()`.
4. Run all required deterministic smoke modes, including the new mode.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_034/01-task.md`
- `state/migration_iterations/iter_034/02-plan.md`
- `state/migration_iterations/iter_034/03-execution.md`
- `state/migration_iterations/iter_034/04-validation.md`
- `state/migration_iterations/iter_034/05-risks-and-decisions.md`
- `state/migration_iterations/iter_034/06-next-iteration.md`
- `state/migration_iterations/iter_034/07-summary.md`
