# Plan

1. Locate the newest long-form adjacency-order guard mode coverage section in `state/copilot_sdk_smoke_test.py`.
2. Add a new exact-once runner for that newest long-form adjacency-order guard mode.
3. Register a new `TRACE_SUMMARY_MODE_SPECS` entry pointing to the new runner.
4. Run the newly registered mode and record validation output.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_147/01-task.md`
- `state/feature_iterations/iter_147/02-plan.md`
- `state/feature_iterations/iter_147/03-execution.md`
- `state/feature_iterations/iter_147/04-validation.md`
- `state/feature_iterations/iter_147/05-risks-and-decisions.md`
- `state/feature_iterations/iter_147/06-next-iteration.md`
- `state/feature_iterations/iter_147/07-summary.md`
