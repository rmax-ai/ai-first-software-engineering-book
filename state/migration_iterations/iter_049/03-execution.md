# Execution

## Commands/tools run
- `view prompts/migration-iteration/execute.md`
- `view state/copilot-sdk-migration-plan.md`
- `view state/migration_iterations/iter_048/06-next-iteration.md`
- `apply_patch` updates in:
  - `state/migration_iterations/iter_044/03-execution.md`
  - `state/migration_iterations/iter_044/04-validation.md`
  - `state/migration_iterations/iter_045/03-execution.md`
  - `state/migration_iterations/iter_045/04-validation.md`
  - `state/migration_iterations/iter_046/03-execution.md`
  - `state/migration_iterations/iter_046/04-validation.md`
- `git --no-pager diff -- ...` for targeted review.

## Files changed
- `state/migration_iterations/iter_044/03-execution.md`
- `state/migration_iterations/iter_044/04-validation.md`
- `state/migration_iterations/iter_045/03-execution.md`
- `state/migration_iterations/iter_045/04-validation.md`
- `state/migration_iterations/iter_046/03-execution.md`
- `state/migration_iterations/iter_046/04-validation.md`
- `state/migration_iterations/iter_049/01-task.md`
- `state/migration_iterations/iter_049/02-plan.md`
- `state/migration_iterations/iter_049/03-execution.md`
- `state/migration_iterations/iter_049/04-validation.md`
- `state/migration_iterations/iter_049/05-risks-and-decisions.md`
- `state/migration_iterations/iter_049/06-next-iteration.md`
- `state/migration_iterations/iter_049/07-summary.md`

## Short rationale per change
- Normalized recent command snippets to `uv run python` so copied guidance matches active runner usage.
- Limited edits to command lines only in recent historical files.
