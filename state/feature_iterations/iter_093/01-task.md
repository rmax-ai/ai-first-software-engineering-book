# Task

## Selected task title
Add a deterministic smoke mode that asserts duplicate-count coverage-guard wrappers delegate to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.

## Why this task now
`state/feature_iterations/iter_092/06-next-iteration.md` prioritized a direct delegation guard to protect the centralized wrapper-helper contract.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that fails when any duplicate-count coverage-guard wrapper does not call `_run_usage_examples_duplicate_count_mode_coverage_guard(`.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with a deterministic description.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-delegation-guard` and capture a PASS result.
