# Task

## Selected task title
Add a smoke guard mode ensuring `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`iter_117/06-next-iteration.md` marked this uniqueness hardening as the next smallest deterministic follow-up after adjacency hardening.

## Acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `...-uniqueness-adjacency-uniqueness-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new uniqueness mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard` and capture PASS output.
