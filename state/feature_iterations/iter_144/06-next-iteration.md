# Next iteration

## Recommended next task
Add uniqueness-count smoke coverage ensuring `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` appears exactly once.

## Why it is next
The new adjacency-order coverage is in place; the smallest follow-up is exact-once registration coverage for that just-added long-form mode.

## Concrete acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts the new long-form mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_145/*.md`
