# Task

## Selected task title
Migrate two additional duplicate-count coverage-guard wrappers to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.

## Why this task now
`state/feature_iterations/iter_080/06-next-iteration.md` identified this as the next smallest unfinished cleanup after the helper was proven on the first two wrappers.

## Acceptance criteria
1. Migrate exactly two more `run_usage_examples_duplicate_count_mode_coverage_guard*` wrappers to the helper.
2. Keep all touched PASS output strings unchanged.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard`
