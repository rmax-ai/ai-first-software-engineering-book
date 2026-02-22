# Plan

1. Add `run_usage_examples_mode_set_coverage_guard_mode()` in `state/copilot_sdk_smoke_test.py` to assert generated non-`stub` usage mode names match expected names by count and set.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so module doc usage, argparse choices/help, and dispatch remain metadata-driven.
3. Run targeted validation for `stub` and the new guard mode.
4. Record execution evidence, risks, and next task across iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_024/01-task.md`
- `state/feature_iterations/iter_024/02-plan.md`
- `state/feature_iterations/iter_024/03-execution.md`
- `state/feature_iterations/iter_024/04-validation.md`
- `state/feature_iterations/iter_024/05-risks-and-decisions.md`
- `state/feature_iterations/iter_024/06-next-iteration.md`
- `state/feature_iterations/iter_024/07-summary.md`
