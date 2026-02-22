# Next iteration

## Recommended next task
Add uniqueness-count smoke coverage for the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode.

## Why it is next
Ordering coverage now exists; the smallest follow-up is a count guard to enforce exactly one registration of this newest mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts the new `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new mode in `TRACE_SUMMARY_MODE_SPECS` for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_137/*.md`
