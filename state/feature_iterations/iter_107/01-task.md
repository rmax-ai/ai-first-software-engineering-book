# Task

## Selected task title
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` is registered immediately after `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`state/feature_iterations/iter_106/06-next-iteration.md` marked this registration-adjacency hardening check as the next smallest deterministic safeguard.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard` and capture PASS output.
