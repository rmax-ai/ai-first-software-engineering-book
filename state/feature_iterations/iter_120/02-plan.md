# Plan

1. Mirror the existing uniqueness guard pattern in `state/copilot_sdk_smoke_test.py` for the latest adjacency guard mode.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` adjacent to the related long-form uniqueness/adjacency guard entries.
3. Run the new mode command to verify deterministic PASS behavior.
4. Record execution, validation evidence, risks, next task, and summary in `state/feature_iterations/iter_120/0{3,4,5,6,7}-*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_120/01-task.md`
- `state/feature_iterations/iter_120/02-plan.md`
- `state/feature_iterations/iter_120/03-execution.md`
- `state/feature_iterations/iter_120/04-validation.md`
- `state/feature_iterations/iter_120/05-risks-and-decisions.md`
- `state/feature_iterations/iter_120/06-next-iteration.md`
- `state/feature_iterations/iter_120/07-summary.md`
