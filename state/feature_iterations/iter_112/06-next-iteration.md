# Next iteration

## Recommended next task
Add a smoke guard mode that enforces adjacency between `usage-examples-order-guard` and `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
This follows the same incremental hardening chain and ensures the newly-added adjacency guard mode remains in the expected registration slot after `usage-examples-order-guard`.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-order-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_113/*.md`
