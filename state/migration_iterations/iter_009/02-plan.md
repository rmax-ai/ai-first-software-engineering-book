# Plan

1. Run kernel in mock LLM mode for a candidate chapter.
2. If run fails, capture exact failure evidence and identify bounded unblock action.
3. Verify chapter eligibility statuses in `state/ledger.json`.
4. Record blocked/pass status against acceptance criteria and recommend one next task.

## Files expected to change
- `state/migration_iterations/iter_009/01-task.md`
- `state/migration_iterations/iter_009/02-plan.md`
- `state/migration_iterations/iter_009/03-execution.md`
- `state/migration_iterations/iter_009/04-validation.md`
- `state/migration_iterations/iter_009/05-risks-and-decisions.md`
- `state/migration_iterations/iter_009/06-next-iteration.md`
- `state/migration_iterations/iter_009/07-summary.md`
