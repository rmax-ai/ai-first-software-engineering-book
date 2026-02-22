# Next iteration

## Recommended next task
Add uniqueness-count smoke coverage for the newly introduced `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard` mode.

## Why it is next
This iteration introduced a new adjacency-order mode; the smallest follow-up is a count assertion that ensures it is registered exactly once.

## Concrete acceptance criteria
1. Add one smoke mode runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_141/*.md`
