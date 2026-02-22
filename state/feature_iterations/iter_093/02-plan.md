# Plan

1. Inspect duplicate-count coverage-guard wrapper functions in `state/copilot_sdk_smoke_test.py` and reuse the existing wrapper-source introspection pattern.
2. Add a new guard mode that enumerates duplicate-count coverage-guard wrappers and asserts each wrapper source includes `_run_usage_examples_duplicate_count_mode_coverage_guard(`.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording so parser choices and generated usage examples include it.
4. Run targeted smoke validation for the new mode and document command/output in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_093/01-task.md`
- `state/feature_iterations/iter_093/02-plan.md`
- `state/feature_iterations/iter_093/03-execution.md`
- `state/feature_iterations/iter_093/04-validation.md`
- `state/feature_iterations/iter_093/05-risks-and-decisions.md`
- `state/feature_iterations/iter_093/06-next-iteration.md`
- `state/feature_iterations/iter_093/07-summary.md`
