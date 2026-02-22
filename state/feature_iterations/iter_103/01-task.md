# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrapper helper argument order (mode-name first, PASS-prefixed message second).

## Why this task now
`state/feature_iterations/iter_102/06-next-iteration.md` identified canonical helper argument ordering as the next deterministic regression guard after positional-only call-shape enforcement.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses wrapper helper calls and asserts arg[0] equals registered mode name and arg[1] starts with canonical PASS prefix.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-arg-order-guard` and capture PASS output.
