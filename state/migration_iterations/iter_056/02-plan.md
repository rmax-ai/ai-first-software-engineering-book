# Plan

1. Confirm the old fallback-error command snippet still exists in `state/migration_iterations/iter_022/01-task.md`.
2. Apply a one-line markdown edit to switch that command to `uv run python`.
3. Run targeted `rg` checks to verify the new snippet exists and the old snippet is gone.
4. Record diff evidence and outcomes in iteration artifacts.

## Files expected to change
- `state/migration_iterations/iter_022/01-task.md`
- `state/migration_iterations/iter_056/01-task.md`
- `state/migration_iterations/iter_056/02-plan.md`
- `state/migration_iterations/iter_056/03-execution.md`
- `state/migration_iterations/iter_056/04-validation.md`
- `state/migration_iterations/iter_056/05-risks-and-decisions.md`
- `state/migration_iterations/iter_056/06-next-iteration.md`
- `state/migration_iterations/iter_056/07-summary.md`
