# Next iteration

## Recommended next task
Add a uniqueness-count smoke guard mode that asserts the new `...order-uniqueness-adjacency-uniqueness-adjacency-order-guard` mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
After adding ordering coverage for the newest adjacency pair, uniqueness coverage for the newly introduced ordering mode is the smallest follow-up to prevent duplicate registrations.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that counts the new `...order-uniqueness-adjacency-uniqueness-adjacency-order-guard` mode and asserts exactly one occurrence.
2. Register that uniqueness-count guard mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_129/*.md`
