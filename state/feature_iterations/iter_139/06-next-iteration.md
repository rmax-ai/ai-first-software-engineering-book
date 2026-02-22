# Next iteration

## Recommended next task
Add adjacency-order smoke coverage for the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode.

## Why it is next
This iteration added uniqueness-count coverage for the newest long-form `...uniqueness-order-guard` mode; the smallest follow-up is an adjacency assertion that places it immediately before the prior `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` appears immediately before `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_140/*.md`
