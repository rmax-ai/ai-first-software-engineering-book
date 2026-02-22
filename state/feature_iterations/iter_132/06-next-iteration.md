# Next iteration

## Recommended next task
Add a uniqueness-count smoke guard mode to ensure the new `...order-uniqueness-order-uniqueness-order-guard` appears exactly once.

## Why it is next
After adding ordering coverage for the new mode, the smallest follow-up is duplicate-prevention coverage for that same mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `...order-uniqueness-order-uniqueness-order-guard` count equals 1 in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `...order-uniqueness-order-uniqueness-order-uniqueness-guard` mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_133/*.md`
