# Task

## Selected task title
Add uniqueness-count smoke coverage ensuring `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` appears exactly once.

## Why this task now
`state/feature_iterations/iter_144/06-next-iteration.md` identified this as the smallest unfinished follow-up after adjacency-order coverage for the newest long-form mode.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` asserting the target long-form mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that uniqueness-count assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
