# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count wrapper helper hardening mode uniqueness before adjacency checks in `TRACE_SUMMARY_MODE_SPECS`.

## Why this task now
`state/feature_iterations/iter_104/06-next-iteration.md` identified uniqueness-before-adjacency as the smallest follow-up after adding the helper mode-order guard.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that counts `usage-examples-duplicate-count-wrapper-helper-positional-only-guard` and `usage-examples-duplicate-count-wrapper-helper-arg-order-guard` in `TRACE_SUMMARY_MODE_SPECS` and requires exactly one each before checking adjacency.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` and capture PASS output.
