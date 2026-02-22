# Next iteration

## Recommended next task
Add a uniqueness-count smoke guard mode for the new `...order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode.

## Why it is next
After adding adjacency-order coverage for the new mode, the smallest follow-up is duplicate-prevention coverage to ensure that mode appears exactly once.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` asserting `...order-uniqueness-order-uniqueness-order-uniqueness-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode in `TRACE_SUMMARY_MODE_SPECS`.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_135/*.md`
