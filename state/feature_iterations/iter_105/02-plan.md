# Plan

1. Add `run_usage_examples_duplicate_count_wrapper_helper_uniqueness_adjacency_guard_mode()` next to existing duplicate-count wrapper helper guard modes in `state/copilot_sdk_smoke_test.py`.
2. Build the check from `TRACE_SUMMARY_MODE_SPECS` mode names, assert each target guard appears exactly once, then assert positional-only is immediately followed by arg-order.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
4. Run the targeted smoke command and capture PASS output for validation evidence.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_105/01-task.md`
- `state/feature_iterations/iter_105/02-plan.md`
- `state/feature_iterations/iter_105/03-execution.md`
- `state/feature_iterations/iter_105/04-validation.md`
- `state/feature_iterations/iter_105/05-risks-and-decisions.md`
- `state/feature_iterations/iter_105/06-next-iteration.md`
- `state/feature_iterations/iter_105/07-summary.md`
