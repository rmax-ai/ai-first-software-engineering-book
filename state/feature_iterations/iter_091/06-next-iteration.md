# Next iteration

## Recommended next task
Add a deterministic smoke check that asserts no `run_usage_examples_duplicate_count_mode_coverage_guard*` wrapper directly calls `_all_mode_specs()`.

## Why it is next
Now that all wrappers in this family delegate to one helper, a guard prevents regression back to copy-paste wrapper bodies.

## Concrete acceptance criteria
1. Add one new smoke mode in `state/copilot_sdk_smoke_test.py` that inspects wrapper source text and fails if a duplicate-count coverage-guard wrapper contains `_all_mode_specs()`.
2. Register the new mode in the mode-spec table with a clear description.
3. Run the new mode with `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and record PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_092/*.md`
