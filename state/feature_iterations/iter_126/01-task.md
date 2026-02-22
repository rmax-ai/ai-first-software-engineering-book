# Task

## Selected task title
Add an adjacency-order smoke guard mode for the newest uniqueness guard pairing.

## Why this task now
`iter_125/06-next-iteration.md` recommends ordering hardening between the newest uniqueness guard mode and newest adjacency-order guard mode.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting the newest `...order-uniqueness-guard` appears immediately before newest `...order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` and capture PASS output.
