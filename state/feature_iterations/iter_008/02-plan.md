# Plan

1. Add one deterministic malformed-`history` fixture mode in `state/copilot_sdk_smoke_test.py` that exercises `_get_latest_trace_summary` shape guards.
2. Wire the new mode through usage docs, CLI choices, and dispatcher branches.
3. Run targeted smoke and compile checks to verify new mode behavior and ensure existing trace-summary paths still pass.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_008/01-task.md`
- `state/feature_iterations/iter_008/02-plan.md`
- `state/feature_iterations/iter_008/03-execution.md`
- `state/feature_iterations/iter_008/04-validation.md`
- `state/feature_iterations/iter_008/05-risks-and-decisions.md`
- `state/feature_iterations/iter_008/06-next-iteration.md`
- `state/feature_iterations/iter_008/07-summary.md`
