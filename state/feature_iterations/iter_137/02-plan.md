# Plan

1. Inspect existing duplicate-count wrapper helper guard runners in `state/copilot_sdk_smoke_test.py` and follow the established naming/ordering pattern.
2. Add one new `run_usage_examples_duplicate_count_wrapper_helper_..._uniqueness_guard_mode` function to assert exactly one registration of the newest `...uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for the new guard mode adjacent to related longest-name guard modes.
4. Execute a targeted smoke run for the new mode and record output.
5. Document execution, validation evidence, risks/decisions, next task, and summary in `state/feature_iterations/iter_137/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_137/01-task.md`
- `state/feature_iterations/iter_137/02-plan.md`
- `state/feature_iterations/iter_137/03-execution.md`
- `state/feature_iterations/iter_137/04-validation.md`
- `state/feature_iterations/iter_137/05-risks-and-decisions.md`
- `state/feature_iterations/iter_137/06-next-iteration.md`
- `state/feature_iterations/iter_137/07-summary.md`
