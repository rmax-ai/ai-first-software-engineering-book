# Task

## Selected task title
Add deterministic coverage for argparse mode-help description synchronization.

## Why this task now
- `state/feature_iterations/iter_018/06-next-iteration.md` identified argparse help text as the remaining drift surface after module-doc coverage was guarded.
- This is the smallest unfinished adjacent task and directly protects user-facing `--help` mode descriptions.

## Acceptance criteria for this iteration
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that verifies mode-help content includes every registered mode description.
2. Keep mode dispatch behavior unchanged.
3. Validate with at least:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-help-coverage-guard`
