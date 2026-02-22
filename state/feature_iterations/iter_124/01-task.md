# Task

## Selected task title
Add an adjacency-order smoke guard for the newest uniqueness guard registration.

## Why this task now
`state/feature_iterations/iter_123/06-next-iteration.md` requested adjacency-order hardening between the two latest uniqueness guard modes.

## Acceptance criteria for this iteration
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting the newest uniqueness guard mode appears immediately before the prior uniqueness guard mode in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new smoke mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard` and capture PASS output.
