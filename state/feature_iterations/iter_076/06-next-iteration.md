# Next iteration

## Recommended next task
Migrate remaining mode-coverage guard functions to use `_mode_action_for_parser`.

## Why it is next
Many guard modes still duplicate parser action lookup; finishing migration will reduce boilerplate and keep assertions consistent.

## Concrete acceptance criteria
1. Replace duplicated `parser._actions` `--mode` lookup in all `run_usage_examples_duplicate_count_mode_coverage_guard*` functions with `_mode_action_for_parser`.
2. Preserve existing assertions and PASS output text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard` and `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard` and record results.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_077/*.md`
