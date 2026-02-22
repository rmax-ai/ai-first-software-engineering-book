# Plan

1. Add `run_usage_examples_duplicate_count_regression_guard_mode` to `state/copilot_sdk_smoke_test.py`.
2. Build synthetic duplicate usage lines from generated usage docs, then parse modes through existing helpers.
3. Compute duplicate counts and assert exact deterministic payload for two duplicated modes.
4. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so docs/help/choices coverage remains automatic.
5. Execute the two required smoke commands and capture results in validation artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_029/01-task.md`
- `state/feature_iterations/iter_029/02-plan.md`
- `state/feature_iterations/iter_029/03-execution.md`
- `state/feature_iterations/iter_029/04-validation.md`
- `state/feature_iterations/iter_029/05-risks-and-decisions.md`
- `state/feature_iterations/iter_029/06-next-iteration.md`
- `state/feature_iterations/iter_029/07-summary.md`
