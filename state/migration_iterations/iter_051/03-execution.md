# Execution

## Commands/tools run
- `view state/copilot-sdk-migration-plan.md`
- `view state/migration_iterations/iter_050/06-next-iteration.md`
- `view state/migration_iterations/iter_022/03-execution.md`
- `view state/migration_iterations/iter_022/04-validation.md`
- `view state/migration_iterations/iter_023/03-execution.md`
- `view state/migration_iterations/iter_023/04-validation.md`
- `apply_patch` on selected historical files in `iter_022` and `iter_023`
- `rg "\`python state/copilot_sdk_smoke_test.py" state/migration_iterations/iter_022 -n`
- `rg "\`python state/copilot_sdk_smoke_test.py" state/migration_iterations/iter_023 -n`
- `git --no-pager diff -- <touched historical files>`
- `git commit -m "Normalize smoke command snippets in iter 022-023"`

## Files changed
- `state/migration_iterations/iter_022/03-execution.md`
- `state/migration_iterations/iter_022/04-validation.md`
- `state/migration_iterations/iter_023/03-execution.md`
- `state/migration_iterations/iter_023/04-validation.md`

## Short rationale per change
- Normalized outdated bare smoke-test command snippets to repository-standard `uv run python` format.
- Kept edits strictly on command lines so historical context and results narratives remain intact.
