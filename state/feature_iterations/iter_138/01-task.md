# Task

## Selected task title
Add adjacency-order smoke coverage for the newest `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode.

## Why this task now
`state/feature_iterations/iter_137/06-next-iteration.md` identified this as the smallest unfinished follow-up after adding uniqueness-count coverage for that newest long-form mode.

## Acceptance criteria
1. Add one smoke mode runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` appears immediately before `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register exactly one new `TRACE_SUMMARY_MODE_SPECS` mode for the adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
