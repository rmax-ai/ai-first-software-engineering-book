# Task

## Selected task title
Add an adjacency-order smoke guard mode for the newest `...order-uniqueness-order-uniqueness-guard` and `...order-uniqueness-order-guard` pair.

## Why this task now
`state/feature_iterations/iter_131/06-next-iteration.md` explicitly requested registration-order adjacency coverage for this newest pair.

## Acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `...order-uniqueness-order-uniqueness-guard` appears immediately before `...order-uniqueness-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `...order-uniqueness-order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard` and capture PASS output.
