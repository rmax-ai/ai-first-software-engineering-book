# Next iteration

## Recommended next task
Add a smoke guard mode that enforces uniqueness for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new order-guard mode should now be protected against accidental duplication, continuing the existing pattern of adding adjacency/order checks followed by uniqueness hardening.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new uniqueness mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_114/*.md`
