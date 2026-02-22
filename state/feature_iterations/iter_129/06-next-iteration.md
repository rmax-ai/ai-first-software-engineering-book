# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode that asserts the new `...order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` registration appears immediately before the corresponding `...order-uniqueness-adjacency-uniqueness-adjacency-order-guard` registration.

## Why it is next
After uniqueness coverage for the newest order-guard mode is in place, adjacency-order coverage is the smallest follow-up to lock deterministic local ordering and prevent accidental tuple drift.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that checks the index of `...order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` is immediately before `...order-uniqueness-adjacency-uniqueness-adjacency-order-guard`.
2. Register one new `...order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_130/*.md`
