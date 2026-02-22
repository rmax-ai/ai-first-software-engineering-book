# Plan

1. Reuse `_run_trace_summary_kernel_mode` to execute kernel trace-summary success and failure variants with `expect_fixture_cleanup=True`.
2. After each run, call `_assert_trace_summary_fixture_root_clean(...)` to verify root-level fixture cleanup symmetry with the non-kernel root-clean mode.
3. Register a new mode in `TRACE_SUMMARY_MODE_SPECS` so CLI choices, generated usage docs, and docstring coverage checks include it automatically.
4. Run targeted smoke validations for the new mode and coverage guards.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_067/01-task.md`
- `state/feature_iterations/iter_067/02-plan.md`
- `state/feature_iterations/iter_067/03-execution.md`
- `state/feature_iterations/iter_067/04-validation.md`
- `state/feature_iterations/iter_067/05-risks-and-decisions.md`
- `state/feature_iterations/iter_067/06-next-iteration.md`
- `state/feature_iterations/iter_067/07-summary.md`
