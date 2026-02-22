# Task

## Selected task title
Extract a shared assertion helper for duplicate-count mode-coverage guard wrappers.

## Why this task now
`state/feature_iterations/iter_077/06-next-iteration.md` marked this as the next smallest unfinished cleanup after parser lookup deduplication.

## Acceptance criteria
1. Add one helper that asserts a target mode exists in argparse `--mode` choices and generated usage examples.
2. Update `run_usage_examples_duplicate_count_mode_coverage_guard_mode` and `run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_mode` to call the helper.
3. Preserve existing PASS output text and run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`.
