# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` to locate the remaining non-helper duplicate-count coverage-guard wrapper.
2. Apply a minimal diff that routes that wrapper through `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` without changing message text.
3. Run targeted `uv run python state/copilot_sdk_smoke_test.py --mode ...` validations for adjacent high-suffix coverage-guard modes.
4. Record execution evidence, risks, and next-step recommendation in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_091/01-task.md`
- `state/feature_iterations/iter_091/02-plan.md`
- `state/feature_iterations/iter_091/03-execution.md`
- `state/feature_iterations/iter_091/04-validation.md`
- `state/feature_iterations/iter_091/05-risks-and-decisions.md`
- `state/feature_iterations/iter_091/06-next-iteration.md`
- `state/feature_iterations/iter_091/07-summary.md`
