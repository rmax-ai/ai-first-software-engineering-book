# Next iteration

## Recommended next task
Extract a shared assertion helper for `run_usage_examples_duplicate_count_mode_coverage_guard*` functions.

## Why it is next
All targeted functions now use the common parser lookup helper, so the next smallest step is removing repeated assertion/usage-check boilerplate.

## Concrete acceptance criteria
1. Introduce one helper that validates parser and usage inclusion for a supplied target mode name.
2. Update at least the base `run_usage_examples_duplicate_count_mode_coverage_guard_mode` and first `..._coverage_guard_mode` wrappers to call the helper.
3. Preserve existing PASS output text and run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_078/*.md`
