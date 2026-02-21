# Execution

## Commands/tools run
- `apply_patch` updated the targeted command snippets in:
  - `state/migration_iterations/iter_026/01-task.md`
  - `state/migration_iterations/iter_026/06-next-iteration.md`
- `git add state/migration_iterations/iter_026/01-task.md state/migration_iterations/iter_026/06-next-iteration.md`
- `git commit -m "Normalize iter_026 smoke command snippets"`
- `rg '\`python state/copilot_sdk_smoke_test.py' state/migration_iterations/iter_026/01-task.md -n`
- `rg '\`python state/copilot_sdk_smoke_test.py' state/migration_iterations/iter_026/06-next-iteration.md -n`
- `git --no-pager show --stat --oneline -1 fb1fae4`

## Files changed
- `state/migration_iterations/iter_026/01-task.md`
- `state/migration_iterations/iter_026/06-next-iteration.md`

## Short rationale per change
- `iter_026/01-task.md`: aligned acceptance-criteria command example with repo convention (`uv run python ...`).
- `iter_026/06-next-iteration.md`: aligned next-task acceptance criteria command examples with the same convention.
