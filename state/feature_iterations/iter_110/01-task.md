# Task

## Selected task title
Add a smoke guard mode enforcing adjacency between `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` and `usage-examples-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`iter_109/06-next-iteration.md` explicitly prioritized this guard to lock deterministic sequencing at the handoff into generic usage-example checks.

## Acceptance criteria
1. Add one new mode in `state/copilot_sdk_smoke_test.py` that asserts immediate adjacency from the uniqueness guard to `usage-examples-order-guard`.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard` and capture PASS output.
