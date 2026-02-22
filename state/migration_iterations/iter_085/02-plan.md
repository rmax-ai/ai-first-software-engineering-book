# Plan

1. Open `state/migration_iterations/iter_083/01-task.md` and confirm the fallback-error escaped snippet still uses legacy `python` wording.
2. Apply the smallest possible one-line edit to normalize the escaped snippet wording to `uv run python`.
3. Run targeted verification commands (`rg`, `git diff`) for the changed file.
4. Record execution, validation, risks, next task, and summary in `state/migration_iterations/iter_085/` artifacts.

## Files expected to change
- `state/migration_iterations/iter_083/01-task.md`
- `state/migration_iterations/iter_085/01-task.md`
- `state/migration_iterations/iter_085/02-plan.md`
- `state/migration_iterations/iter_085/03-execution.md`
- `state/migration_iterations/iter_085/04-validation.md`
- `state/migration_iterations/iter_085/05-risks-and-decisions.md`
- `state/migration_iterations/iter_085/06-next-iteration.md`
- `state/migration_iterations/iter_085/07-summary.md`
