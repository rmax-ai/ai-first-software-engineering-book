# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode that asserts the newest `...order-uniqueness-adjacency-uniqueness-adjacency-guard` mode appears immediately before the nearest prior `...order-uniqueness-adjacency-guard` mode in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new uniqueness-count guard now confirms presence uniqueness; ordering coverage is the smallest follow-up to keep newest and prior guard modes deterministically adjacent.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that compares indices of the newest `...order-uniqueness-adjacency-uniqueness-adjacency-guard` mode and prior `...order-uniqueness-adjacency-guard` mode, asserting immediate adjacency.
2. Register that new adjacency-order guard mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_128/*.md`
