# Plan

1. Add one deterministic malformed latest-`history`-entry mode in `state/copilot_sdk_smoke_test.py` that exercises `_get_latest_trace_summary` latest-entry shape guard.
2. Wire the new mode through usage text, CLI choices, help text, and dispatcher branches.
3. Run targeted smoke and compile checks to verify the new mode and confirm neighboring trace-summary modes still pass.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_009/01-task.md`
- `state/feature_iterations/iter_009/02-plan.md`
- `state/feature_iterations/iter_009/03-execution.md`
- `state/feature_iterations/iter_009/04-validation.md`
- `state/feature_iterations/iter_009/05-risks-and-decisions.md`
- `state/feature_iterations/iter_009/06-next-iteration.md`
- `state/feature_iterations/iter_009/07-summary.md`
