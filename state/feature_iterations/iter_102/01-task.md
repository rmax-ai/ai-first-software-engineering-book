# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrapper helper call shape uses positional args only (no keyword args).

## Why this task now
`state/feature_iterations/iter_101/06-next-iteration.md` marked positional-only helper call-shape validation as the next smallest deterministic hardening step.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` is called with exactly two positional args and zero keyword args.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-positional-only-guard` and capture PASS output.
