# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-single-delegation-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-single-delegation-guard mode validates duplicate-count coverage-guard wrappers call _run_usage_examples_duplicate_count_mode_coverage_guard(...) exactly once`

## Pass/fail against acceptance criteria
1. **Pass** — new mode fails when any duplicate-count coverage-guard wrapper source has helper call count not equal to one.
2. **Pass** — mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. **Pass** — targeted smoke command completed successfully with PASS output.
