# Execution

## Commands/tools run
1. `python - <<'PY' ...` to inspect chapter statuses in `state/ledger.json`.
2. `python state/kernel.py --chapter-id 01-paradigm-shift`
3. `python state/kernel.py --chapter-id 01-paradigm-shift --llm --llm-provider mock`
4. `git restore -- state/ledger.json state/metrics.json` (to keep minimal diffs after failed validation attempts).

## Files changed
- `state/migration_iterations/iter_013/01-task.md`
- `state/migration_iterations/iter_013/02-plan.md`
- `state/migration_iterations/iter_013/03-execution.md`
- `state/migration_iterations/iter_013/04-validation.md`
- `state/migration_iterations/iter_013/05-risks-and-decisions.md`
- `state/migration_iterations/iter_013/06-next-iteration.md`
- `state/migration_iterations/iter_013/07-summary.md`

## Short rationale per change
- Captured deterministic, command-backed evidence for the remaining kernel mock regression task.
- Preserved minimal diff by reverting transient ledger/metrics mutations from failed runs.
