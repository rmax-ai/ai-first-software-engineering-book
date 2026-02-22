# Next iteration

## Recommended next task
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new adjacency-order guard now checks ordering but not duplication; a uniqueness check closes that deterministic registration gap.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that asserts count(`usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard`) == 1 in `TRACE_SUMMARY_MODE_SPECS`.
2. Register that mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_109/*.md`
