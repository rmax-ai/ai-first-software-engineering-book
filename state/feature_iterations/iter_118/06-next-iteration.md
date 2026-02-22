# Next iteration

## Recommended next task
Add a smoke guard mode ensuring `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
After uniqueness hardening, adjacency hardening for the newly added uniqueness mode is the smallest deterministic follow-up to prevent registration-order drift.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting the new `...-uniqueness-adjacency-uniqueness-guard` mode appears immediately before `...-uniqueness-adjacency-uniqueness-guard` predecessor mode.
2. Register the new adjacency mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_119/*.md`
