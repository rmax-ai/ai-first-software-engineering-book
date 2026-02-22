# Task

## Selected task title
Add a smoke guard mode that enforces `TRACE_SUMMARY_MODE_SPECS` keeps duplicate-count wrapper helper hardening modes in deterministic adjacency order (positional-only immediately followed by arg-order).

## Why this task now
`state/feature_iterations/iter_103/06-next-iteration.md` identified mode-order lock-in as the smallest follow-up after adding the helper arg-order guard.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-positional-only-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-arg-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-mode-order-guard` and capture PASS output.
