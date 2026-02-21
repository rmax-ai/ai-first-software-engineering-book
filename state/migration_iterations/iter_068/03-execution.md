# Execution

## Commands/tools run
1. `view state/migration_iterations/iter_067/06-next-iteration.md` to load recommended next task.
2. `view state/migration_iterations/iter_064/06-next-iteration.md` to inspect current acceptance criteria text.
3. `apply_patch` on `state/migration_iterations/iter_064/06-next-iteration.md` to normalize the snippet wording.
4. `rg`/`git --no-pager diff` verification commands on the edited file.

## Files changed
- `state/migration_iterations/iter_064/06-next-iteration.md`
- `state/migration_iterations/iter_068/01-task.md`
- `state/migration_iterations/iter_068/02-plan.md`
- `state/migration_iterations/iter_068/03-execution.md`
- `state/migration_iterations/iter_068/04-validation.md`
- `state/migration_iterations/iter_068/05-risks-and-decisions.md`
- `state/migration_iterations/iter_068/06-next-iteration.md`
- `state/migration_iterations/iter_068/07-summary.md`

## Short rationale per change
- Updated `iter_064` acceptance-criteria snippet wording to align with the migration convention (`uv run python`).
- Added `iter_068` artifacts to capture this iteration’s single-task execution, validation evidence, decisions, and handoff.
