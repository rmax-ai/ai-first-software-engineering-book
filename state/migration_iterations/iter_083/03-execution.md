# Execution

## Commands/tools run
- `rg -nF 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_081/01-task.md`
- `apply_patch` update in `state/migration_iterations/iter_081/01-task.md`
- `git --no-pager diff -- state/migration_iterations/iter_081/01-task.md`
- `git add state/migration_iterations/iter_081/01-task.md && git commit ...`
- `git --no-pager show HEAD^:state/migration_iterations/iter_081/01-task.md | rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`'`
- `rg -nF '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_081/01-task.md`

## Files changed
- `state/migration_iterations/iter_081/01-task.md`

## Short rationale per change
- Replaced the remaining escaped legacy snippet wording with the normalized `uv run python` form to keep migration evidence text consistent.
