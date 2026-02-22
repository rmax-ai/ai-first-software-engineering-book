# Task

## Selected task title
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`state/feature_iterations/iter_108/06-next-iteration.md` explicitly requested this uniqueness follow-up to close the remaining deterministic registration gap.

## Acceptance criteria
1. `state/copilot_sdk_smoke_test.py` adds one mode for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` asserting exactly one registry entry for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard`.
2. The new mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` passes.
