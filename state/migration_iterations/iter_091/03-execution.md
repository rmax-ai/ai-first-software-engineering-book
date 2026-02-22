# Execution

## Commands/tools run
1. `view state/copilot-sdk-migration-plan.md`
2. `view state/migration_iterations/iter_090/06-next-iteration.md`
3. Updated one acceptance-criteria line in `state/migration_iterations/iter_080/01-task.md`.
4. `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_080/01-task.md`
5. `rg -nF 'confirms the normalized snippet mention' state/migration_iterations/iter_080/01-task.md`
6. `git --no-pager diff -- state/migration_iterations/iter_080/01-task.md`

## Files changed
- `state/migration_iterations/iter_080/01-task.md`
- `state/migration_iterations/iter_091/01-task.md`
- `state/migration_iterations/iter_091/02-plan.md`
- `state/migration_iterations/iter_091/03-execution.md`
- `state/migration_iterations/iter_091/04-validation.md`
- `state/migration_iterations/iter_091/05-risks-and-decisions.md`
- `state/migration_iterations/iter_091/06-next-iteration.md`
- `state/migration_iterations/iter_091/07-summary.md`

## Short rationale per change
- Corrected one residual evidence phrase so wording matches the already-normalized snippet mention.
- Added required iteration artifacts with scoped validation evidence and one concrete follow-up task.
