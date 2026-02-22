# Task

## Selected task title
Add an adjacency-order smoke guard mode for the newest uniqueness-adjacency-order mode pair.

## Why this task now
`state/feature_iterations/iter_129/06-next-iteration.md` prioritized locking local registration order between the newest `...order-uniqueness-guard` and `...order-guard` entries in `TRACE_SUMMARY_MODE_SPECS`.

## Acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `...order-uniqueness-guard` appears immediately before `...order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `...order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard` and capture PASS output.
