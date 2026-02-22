# Task

## Selected task title
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` is registered immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`state/feature_iterations/iter_107/06-next-iteration.md` called for this exact adjacency hardening step to extend deterministic ordering checks for duplicate-count helper guard modes.

## Acceptance criteria
1. `state/copilot_sdk_smoke_test.py` adds one mode function named for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard` asserting immediate adjacency from uniqueness-order to uniqueness-order-adjacency guard.
2. The new mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard` passes.
