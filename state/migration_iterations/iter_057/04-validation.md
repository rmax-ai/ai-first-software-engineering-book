# Validation

## Verification commands run
1. `rg '\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_021/06-next-iteration.md -n`
2. `rg '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_021/06-next-iteration.md -n`
3. `git --no-pager diff -- state/migration_iterations/iter_021/06-next-iteration.md`

## Observed outputs/results
- Command 1: one match at line 10 with the normalized `uv run python` snippet.
- Command 2: no matches.
- Command 3: one-line diff only; non-command narrative unchanged.

## Pass/fail against acceptance criteria
- Required snippet replacement in `iter_021/06-next-iteration.md`: PASS.
- Non-command narrative unchanged: PASS.
- Targeted search/diff evidence captured: PASS.
