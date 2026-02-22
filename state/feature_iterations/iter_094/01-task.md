# Task

## Selected task title
Add a deterministic smoke mode that asserts duplicate-count coverage-guard wrappers call `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` exactly once.

## Why this task now
`state/feature_iterations/iter_093/06-next-iteration.md` prioritized enforcing single helper invocation per wrapper to prevent duplicate or conflicting delegation calls.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that fails when any duplicate-count coverage-guard wrapper has zero or multiple `_run_usage_examples_duplicate_count_mode_coverage_guard(` occurrences.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-single-delegation-guard` and capture PASS output.
