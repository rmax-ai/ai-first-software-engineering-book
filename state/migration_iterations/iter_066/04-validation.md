# Validation

## Verification commands run
1. `rg -n '`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`' state/migration_iterations/iter_055/06-next-iteration.md || true`
2. `rg -n 'uv run python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_055/06-next-iteration.md`
3. `git --no-pager show --stat --oneline b0f3604 -- state/migration_iterations/iter_055/06-next-iteration.md`

## Observed results
- Normalized snippet found at line 10: `Ensure \`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\` is used ...`.
- Commit `b0f3604` shows `state/migration_iterations/iter_055/06-next-iteration.md | 2 +-` with one insertion and one deletion.

## Acceptance criteria check
- Legacy bare snippet removed: **pass**
- Normalized `uv run python` snippet present: **pass**
- Targeted evidence captured: **pass**
