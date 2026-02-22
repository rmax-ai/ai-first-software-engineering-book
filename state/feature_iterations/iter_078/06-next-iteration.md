# Next iteration

## Recommended next task
Migrate all remaining `run_usage_examples_duplicate_count_mode_coverage_guard*` wrappers to `_assert_mode_in_parser_and_usage_examples(...)`.

## Why it is next
The helper is now proven in the base and first wrapper, so extending it to the remaining wrappers is the next smallest consistency cleanup.

## Concrete acceptance criteria
1. Replace duplicated parser/usage inclusion assertions with helper calls in every remaining `run_usage_examples_duplicate_count_mode_coverage_guard*` wrapper.
2. Preserve existing PASS output text for all touched wrappers.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_079/*.md`
