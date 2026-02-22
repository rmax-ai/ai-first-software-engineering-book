# Task

## Selected task title
Add uniqueness-count smoke coverage for `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`.

## Why this task now
`state/feature_iterations/iter_142/06-next-iteration.md` marked this as the smallest unfinished follow-up after adding adjacency-order coverage.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
