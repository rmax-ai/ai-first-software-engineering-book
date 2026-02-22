# Task

## Selected task title
Add uniqueness smoke guard for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard` registration.

## Why this task now
`iter_110/06-next-iteration.md` recommended locking uniqueness for the newly-added adjacency guard mode to prevent duplicate registration drift.

## Acceptance criteria
1. Add one guard mode in `state/copilot_sdk_smoke_test.py` that asserts this mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register that new guard mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` with PASS output.
