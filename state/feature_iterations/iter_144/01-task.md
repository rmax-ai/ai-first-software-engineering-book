# Task

## Selected task title
Add adjacency-order smoke coverage ensuring `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`.

## Why this task now
`state/feature_iterations/iter_143/06-next-iteration.md` marked this as the smallest unfinished follow-up after uniqueness-count coverage for the newest long-form mode.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` asserting adjacency order for the two target long-form modes.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for the new adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
