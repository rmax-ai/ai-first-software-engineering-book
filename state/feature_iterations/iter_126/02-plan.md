# Plan

1. Inspect existing newest adjacency-order and uniqueness guard helper functions in `state/copilot_sdk_smoke_test.py`.
2. Add one new smoke mode function to assert adjacency ordering between newest uniqueness and adjacency-order guard mode names.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description and ensure target mode ordering satisfies the new assertion.
4. Run the targeted smoke mode command and record evidence.
5. Write iteration artifacts for execution, validation, risks, next task, and summary.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_126/01-task.md`
- `state/feature_iterations/iter_126/02-plan.md`
- `state/feature_iterations/iter_126/03-execution.md`
- `state/feature_iterations/iter_126/04-validation.md`
- `state/feature_iterations/iter_126/05-risks-and-decisions.md`
- `state/feature_iterations/iter_126/06-next-iteration.md`
- `state/feature_iterations/iter_126/07-summary.md`
