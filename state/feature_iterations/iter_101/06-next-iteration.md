# Next iteration

## Recommended next task
Add a guard mode that enforces duplicate-count coverage-guard wrapper helper call shape uses positional args only (no keyword args).

## Why it is next
After locking helper argument literals, positional-only call-shape enforcement is the smallest adjacent deterministic hardening step for wrapper delegation structure.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` is called with exactly two positional args and zero keyword args.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-positional-only-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_102/*.md`
