# Plan

1. Update `state/copilot_sdk_smoke_test.py` with a helper that asserts the trace-summary fixture root has no residual subdirectories.
2. Add a new mode function that runs the existing non-kernel trace-summary variants with fixture cleanup enabled and calls the new root-clean assertion after each run.
3. Register the mode in `TRACE_SUMMARY_MODE_SPECS` so parser choices/help and generated docs stay synchronized.
4. Run targeted smoke validation for the new mode and existing guard modes to confirm behavior remains stable.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_066/03-execution.md`
- `state/feature_iterations/iter_066/04-validation.md`
- `state/feature_iterations/iter_066/05-risks-and-decisions.md`
- `state/feature_iterations/iter_066/06-next-iteration.md`
- `state/feature_iterations/iter_066/07-summary.md`
