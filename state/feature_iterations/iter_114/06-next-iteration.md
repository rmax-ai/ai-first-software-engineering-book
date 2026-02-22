# Next iteration

## Recommended next task
Add an order smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` appears immediately before `usage-examples-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
After uniqueness hardening, the next deterministic step is adjacency hardening for the newly added uniqueness guard mode.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` is directly adjacent to `usage-examples-order-guard`.
2. Register the new adjacency mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_115/*.md`
