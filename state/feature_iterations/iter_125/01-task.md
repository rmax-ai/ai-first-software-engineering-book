# Task

## Selected task title
Add a uniqueness smoke guard for the newest adjacency-order guard mode.

## Why this task now
`state/feature_iterations/iter_124/06-next-iteration.md` requested a deterministic uniqueness assertion for the newest adjacency-order guard registration.

## Acceptance criteria for this iteration
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that counts `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard` and asserts the count is exactly 1.
2. Register a new uniqueness smoke mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` and capture PASS output.
