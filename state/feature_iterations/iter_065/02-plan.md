# Plan

1. Update `run_trace_summary_mode` in `state/copilot_sdk_uv_smoke.py` so the fixture cleanup target is set for both kernel and non-kernel fixture repositories.
2. Extend `state/copilot_sdk_smoke_test.py` with a non-kernel fixture-repo constant and helper wrapper that can assert cleanup after each uv smoke invocation.
3. Add a single aggregate mode that executes `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase` without `--run-kernel-for-trace-summary`, asserting cleanup each time.
4. Register the new mode in `TRACE_SUMMARY_MODE_SPECS`.
5. Run targeted smoke validations and capture PASS outputs.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_065/01-task.md`
- `state/feature_iterations/iter_065/02-plan.md`
- `state/feature_iterations/iter_065/03-execution.md`
- `state/feature_iterations/iter_065/04-validation.md`
- `state/feature_iterations/iter_065/05-risks-and-decisions.md`
- `state/feature_iterations/iter_065/06-next-iteration.md`
- `state/feature_iterations/iter_065/07-summary.md`
