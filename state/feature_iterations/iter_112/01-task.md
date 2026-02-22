# Task

## Selected task title
Add adjacency smoke guard for `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` ordering.

## Why this task now
`state/feature_iterations/iter_111/06-next-iteration.md` prioritized enforcing adjacency between the newest uniqueness guard mode and `usage-examples-order-guard`.

## Acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` appears immediately before `usage-examples-order-guard`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` with PASS output.
