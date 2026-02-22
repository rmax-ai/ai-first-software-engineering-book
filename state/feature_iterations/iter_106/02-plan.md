# Plan

1. Add `run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_guard_mode()` beside existing duplicate-count wrapper helper hardening guard modes.
2. Build the check from `TRACE_SUMMARY_MODE_SPECS` names: assert both target modes exist, then assert uniqueness-adjacency guard index is exactly one after mode-order guard index.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic naming/description.
4. Run the targeted smoke mode and capture output in validation evidence.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_106/01-task.md`
- `state/feature_iterations/iter_106/02-plan.md`
- `state/feature_iterations/iter_106/03-execution.md`
- `state/feature_iterations/iter_106/04-validation.md`
- `state/feature_iterations/iter_106/05-risks-and-decisions.md`
- `state/feature_iterations/iter_106/06-next-iteration.md`
- `state/feature_iterations/iter_106/07-summary.md`
