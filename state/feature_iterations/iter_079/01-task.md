# Task

## Selected task title
Migrate all remaining duplicate-count mode coverage-guard wrappers to the shared parser/usage assertion helper.

## Why this task now
`state/feature_iterations/iter_078/06-next-iteration.md` identified this as the next smallest unfinished cleanup after proving the helper in the base and first wrapper.

## Acceptance criteria
1. Replace duplicated parser-choice and usage-example inclusion assertions with `_assert_mode_in_parser_and_usage_examples(...)` in every remaining `run_usage_examples_duplicate_count_mode_coverage_guard*` wrapper.
2. Preserve existing PASS output text for all touched wrappers.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard`
