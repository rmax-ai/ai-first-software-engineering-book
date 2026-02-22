# Task

## Selected task title
Add a uniqueness smoke guard for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard`.

## Why this task now
`state/feature_iterations/iter_115/06-next-iteration.md` prioritized uniqueness hardening to ensure the newly added adjacency guard mode cannot be duplicated in `TRACE_SUMMARY_MODE_SPECS`.

## Acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` appears exactly once.
2. Register the new uniqueness mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard` and capture PASS output.
