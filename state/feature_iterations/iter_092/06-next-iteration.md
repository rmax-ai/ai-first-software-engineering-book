# Next iteration

## Recommended next task
Add a guard mode that asserts every duplicate-count coverage-guard wrapper delegates to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.

## Why it is next
The new `_all_mode_specs()` regression guard prevents one historical failure mode; this follow-up will enforce the intended helper delegation contract directly.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that fails if any duplicate-count coverage-guard wrapper body lacks `_run_usage_examples_duplicate_count_mode_coverage_guard(`.
2. Register the mode in the mode-spec table with a deterministic description.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and record PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_093/*.md`
