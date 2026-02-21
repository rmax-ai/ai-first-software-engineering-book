# Plan

1. Add a new `close-idempotency` deterministic mode in `state/copilot_sdk_smoke_test.py` using the shutdown failure path.
2. Ensure first `close()` raises expected failure details and second `close()` succeeds without additional mutation checks failing.
3. Update CLI mode choices/help text to expose the new mode.
4. Run all deterministic non-live smoke modes to confirm unchanged outputs plus new mode pass.
5. Record evidence and write iteration handoff artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_036/01-task.md`
- `state/migration_iterations/iter_036/02-plan.md`
- `state/migration_iterations/iter_036/03-execution.md`
- `state/migration_iterations/iter_036/04-validation.md`
- `state/migration_iterations/iter_036/05-risks-and-decisions.md`
- `state/migration_iterations/iter_036/06-next-iteration.md`
- `state/migration_iterations/iter_036/07-summary.md`
