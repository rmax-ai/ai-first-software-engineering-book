# Task

## Selected task title
Add uniqueness-count smoke coverage for the newest `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode.

## Why this task now
`state/feature_iterations/iter_136/06-next-iteration.md` identifies this as the smallest unfinished follow-up after adding adjacency-order coverage for that newest mode.

## Acceptance criteria
1. Add one smoke mode runner in `state/copilot_sdk_smoke_test.py` that asserts the newest `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
