# Plan

1. Inspect existing long-form duplicate-count wrapper helper guard runners in `state/copilot_sdk_smoke_test.py` and follow the established naming and placement pattern.
2. Add one new `run_usage_examples_duplicate_count_wrapper_helper_..._uniqueness_order_guard_mode` function that checks adjacency between the newest `...-uniqueness-guard` mode and the prior `...-order-guard` mode.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for this adjacency-order assertion mode without breaking existing registration adjacency.
4. Run the targeted smoke mode command and keep only a minimal corrective edit if the first run fails.
5. Record execution evidence, validation results, risks/decisions, next iteration recommendation, and summary in `state/feature_iterations/iter_138/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_138/01-task.md`
- `state/feature_iterations/iter_138/02-plan.md`
- `state/feature_iterations/iter_138/03-execution.md`
- `state/feature_iterations/iter_138/04-validation.md`
- `state/feature_iterations/iter_138/05-risks-and-decisions.md`
- `state/feature_iterations/iter_138/06-next-iteration.md`
- `state/feature_iterations/iter_138/07-summary.md`
