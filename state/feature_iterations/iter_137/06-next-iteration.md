# Next iteration

## Recommended next task
Add adjacency-order smoke coverage for the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode.

## Why it is next
This iteration added count coverage for the newest long-form guard; the smallest follow-up is enforcing adjacency ordering between this new count mode and the prior longest count mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode appears immediately before the prior `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new mode in `TRACE_SUMMARY_MODE_SPECS` for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_138/*.md`
