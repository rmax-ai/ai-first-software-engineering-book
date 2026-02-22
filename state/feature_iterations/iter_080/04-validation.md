# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`

## Observed outputs/results
- Command 1: `PASS: usage-examples-duplicate-count-mode-coverage-guard mode validates duplicate-count regression mode coverage`
- Command 2: `PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard mode coverage`

## Pass/fail against acceptance criteria
1. **Pass** — helper `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` was added and accepts target mode + PASS text.
2. **Pass** — exactly two wrappers were migrated to the helper.
3. **Pass** — both required smoke commands succeeded.
