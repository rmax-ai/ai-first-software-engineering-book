# Next iteration

## Recommended next task
Add a guard mode that validates duplicate-count coverage-guard wrappers call `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` exactly once per wrapper.

## Why it is next
The new delegation guard confirms helper usage exists; this follow-up will prevent future wrappers from adding redundant or conflicting helper invocations.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that inspects duplicate-count coverage-guard wrapper source and fails unless each wrapper contains exactly one `_run_usage_examples_duplicate_count_mode_coverage_guard(` occurrence.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with a deterministic description.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and record PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_094/*.md`
