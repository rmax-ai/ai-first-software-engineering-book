# Plan

1. Add `run_usage_examples_duplicate_count_wrapper_helper_mode_order_guard_mode()` near existing duplicate-count wrapper helper guard modes in `state/copilot_sdk_smoke_test.py`.
2. Build the new check from `TRACE_SUMMARY_MODE_SPECS` mode names only, then assert positional-only guard index is immediately followed by arg-order guard index.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
4. Run the targeted smoke command for the new mode and capture output for validation.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_104/01-task.md`
- `state/feature_iterations/iter_104/02-plan.md`
- `state/feature_iterations/iter_104/03-execution.md`
- `state/feature_iterations/iter_104/04-validation.md`
- `state/feature_iterations/iter_104/05-risks-and-decisions.md`
- `state/feature_iterations/iter_104/06-next-iteration.md`
- `state/feature_iterations/iter_104/07-summary.md`
