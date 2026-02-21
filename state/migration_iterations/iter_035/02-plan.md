# Plan

1. Inspect duplicated setup/teardown logic in `state/copilot_sdk_smoke_test.py` shutdown-related modes.
2. Extract one setup helper and one teardown helper with equivalent behavior.
3. Update four shutdown-related mode handlers to reuse helpers.
4. Run deterministic smoke validations for all existing non-live modes.
5. Record evidence and handoff for next iteration.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_035/01-task.md`
- `state/migration_iterations/iter_035/02-plan.md`
- `state/migration_iterations/iter_035/03-execution.md`
- `state/migration_iterations/iter_035/04-validation.md`
- `state/migration_iterations/iter_035/05-risks-and-decisions.md`
- `state/migration_iterations/iter_035/06-next-iteration.md`
- `state/migration_iterations/iter_035/07-summary.md`
