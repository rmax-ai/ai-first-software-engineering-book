# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-delegation-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-delegation-guard mode validates duplicate-count coverage-guard wrappers delegate to _run_usage_examples_duplicate_count_mode_coverage_guard(...)`

## Pass/fail against acceptance criteria
1. **Pass** — new mode fails if any duplicate-count coverage-guard wrapper source is missing `_run_usage_examples_duplicate_count_mode_coverage_guard(`.
2. **Pass** — mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. **Pass** — targeted smoke command completed successfully with PASS output.
