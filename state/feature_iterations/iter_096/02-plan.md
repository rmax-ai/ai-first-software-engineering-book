# Plan

1. Inspect current duplicate-count wrapper guards and identify insertion point for a mode-name literal guard.
2. Add a new guard function that parses wrapper helper calls and compares first argument literals against registered mode names.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` near related duplicate-count wrapper guards.
4. Run targeted smoke validation for the new mode and one impacted duplicate-count mode.
5. Record execution, risks, and next recommendation in this iteration folder.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_096/01-task.md`
- `state/feature_iterations/iter_096/02-plan.md`
- `state/feature_iterations/iter_096/03-execution.md`
- `state/feature_iterations/iter_096/04-validation.md`
- `state/feature_iterations/iter_096/05-risks-and-decisions.md`
- `state/feature_iterations/iter_096/06-next-iteration.md`
- `state/feature_iterations/iter_096/07-summary.md`
