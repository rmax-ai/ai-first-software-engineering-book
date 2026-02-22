# Task

## Selected task title
Add adjacency-order smoke coverage ensuring `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard`.

## Why this task now
`state/feature_iterations/iter_141/06-next-iteration.md` identified this as the smallest unfinished follow-up after adding uniqueness-count coverage for the new long-form adjacency-order mode.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
