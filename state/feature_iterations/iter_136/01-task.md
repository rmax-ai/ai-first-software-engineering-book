# Task

## Selected task title
Add adjacency-order smoke guard coverage for the newest uniqueness-order guard mode.

## Why this task now
`state/feature_iterations/iter_135/06-next-iteration.md` recommends this as the smallest unfinished follow-up after adding uniqueness-count coverage for the newest mode.

## Acceptance criteria
1. Add one smoke guard runner in `state/copilot_sdk_smoke_test.py` that checks newest `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` ordering against the prior guard mode.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for that mode.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
