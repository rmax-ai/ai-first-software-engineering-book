# Next iteration

## Recommended next task
Add a uniqueness smoke guard mode ensuring `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new adjacency mode is now order-hardened; uniqueness hardening is the next deterministic safeguard against duplicate registration drift.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` count is exactly 1.
2. Register the new uniqueness mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_116/*.md`
