# Plan

1. Inspect the newest long-form duplicate-count wrapper helper runners near the prior adjacency-order addition in `state/copilot_sdk_smoke_test.py`.
2. Add one new `run_usage_examples_duplicate_count_wrapper_helper_..._uniqueness_guard_mode` function that counts the new `...-uniqueness-order-guard` mode and asserts the count is exactly one.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for the new uniqueness-count runner.
4. Run the targeted smoke mode command for the new mode and capture output.
5. Record execution, validation, risks/decisions, next task, and summary in `state/feature_iterations/iter_139/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_139/01-task.md`
- `state/feature_iterations/iter_139/02-plan.md`
- `state/feature_iterations/iter_139/03-execution.md`
- `state/feature_iterations/iter_139/04-validation.md`
- `state/feature_iterations/iter_139/05-risks-and-decisions.md`
- `state/feature_iterations/iter_139/06-next-iteration.md`
- `state/feature_iterations/iter_139/07-summary.md`
