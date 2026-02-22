# Plan

1. Update `state/copilot_sdk_uv_smoke.py` so kernel-backed trace-summary fixture repos are deleted in a `finally` block after each run.
2. Extend `_run_trace_summary_kernel_mode` in `state/copilot_sdk_smoke_test.py` with an optional cleanup assertion for `state/.smoke_fixtures/trace_summary/kernel_repo`.
3. Add one deterministic mode that executes all four kernel-backed trace-summary variants and enables cleanup assertions for each invocation.
4. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so parser choices and generated docs remain synchronized.
5. Run targeted smoke validations and capture PASS evidence.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_064/01-task.md`
- `state/feature_iterations/iter_064/02-plan.md`
- `state/feature_iterations/iter_064/03-execution.md`
- `state/feature_iterations/iter_064/04-validation.md`
- `state/feature_iterations/iter_064/05-risks-and-decisions.md`
- `state/feature_iterations/iter_064/06-next-iteration.md`
- `state/feature_iterations/iter_064/07-summary.md`
