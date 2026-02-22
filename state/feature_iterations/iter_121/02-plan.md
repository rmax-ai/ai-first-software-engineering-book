# Plan

1. Mirror the existing adjacency guard pattern in `state/copilot_sdk_smoke_test.py` for the latest uniqueness guard mode.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` directly before the related uniqueness guard entry.
3. Run the new mode command to verify deterministic PASS behavior.
4. Record execution, validation evidence, risks, next task, and summary in `state/feature_iterations/iter_121/0{3,4,5,6,7}-*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_121/01-task.md`
- `state/feature_iterations/iter_121/02-plan.md`
- `state/feature_iterations/iter_121/03-execution.md`
- `state/feature_iterations/iter_121/04-validation.md`
- `state/feature_iterations/iter_121/05-risks-and-decisions.md`
- `state/feature_iterations/iter_121/06-next-iteration.md`
- `state/feature_iterations/iter_121/07-summary.md`
