# Task

## Selected task title
Add a uniqueness-count smoke guard mode for the newest uniqueness-adjacency guard pairing.

## Why this task now
`iter_126/06-next-iteration.md` prioritized hardening uniqueness coverage for the newly added `...order-uniqueness-adjacency-guard` mode.

## Acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts the new `...order-uniqueness-adjacency-guard` mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new uniqueness-count mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` and capture PASS output.
