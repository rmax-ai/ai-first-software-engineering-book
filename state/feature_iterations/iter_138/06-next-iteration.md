# Next iteration

## Recommended next task
Add uniqueness-count smoke coverage for the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` adjacency-order mode.

## Why it is next
This iteration added adjacency-order enforcement for the newest long-form uniqueness guard pair; the smallest follow-up is enforcing single-registration uniqueness for the new adjacency-order mode itself.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_139/*.md`
