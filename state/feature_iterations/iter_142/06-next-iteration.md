# Next iteration

## Recommended next task
Add uniqueness-count smoke coverage for the new `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` mode.

## Why it is next
This iteration added adjacency-order coverage; the smallest follow-up is a count guard to ensure the new mode remains registered exactly once.

## Concrete acceptance criteria
1. Add one smoke mode runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_143/*.md`
