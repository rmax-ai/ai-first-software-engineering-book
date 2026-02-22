# Next iteration

## Recommended next task
Add a smoke guard mode that asserts `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard` is registered exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new adjacency guard now enforces relative order, but uniqueness should also be locked to prevent duplicate registration drift.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that counts occurrences of `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS` and asserts exactly one.
2. Register that mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_111/*.md`
