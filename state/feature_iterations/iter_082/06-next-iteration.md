# Next iteration

## Recommended next task
Migrate two more duplicate-count coverage-guard wrappers to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.

## Why it is next
The helper rollout is intentionally incremental; another two-wrapper slice continues cleanup with low risk and clear validation.

## Concrete acceptance criteria
1. Migrate exactly two additional `run_usage_examples_duplicate_count_mode_coverage_guard*` wrappers to the helper.
2. Keep all touched PASS output strings unchanged.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_083/*.md`
