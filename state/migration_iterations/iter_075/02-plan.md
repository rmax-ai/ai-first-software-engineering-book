# Plan

1. Confirm the legacy fallback-timeout snippet mention exists in `state/migration_iterations/iter_071/01-task.md`.
2. Apply a one-line normalization replacing the backticked bare `python` snippet text with `uv run python` wording.
3. Run focused `rg` checks and inspect scoped git diff for the edited file.
4. Record execution and validation evidence in iteration artifacts.

## Files expected to change
- `state/migration_iterations/iter_071/01-task.md`
- `state/migration_iterations/iter_075/01-task.md`
- `state/migration_iterations/iter_075/02-plan.md`
- `state/migration_iterations/iter_075/03-execution.md`
- `state/migration_iterations/iter_075/04-validation.md`
- `state/migration_iterations/iter_075/05-risks-and-decisions.md`
- `state/migration_iterations/iter_075/06-next-iteration.md`
- `state/migration_iterations/iter_075/07-summary.md`
