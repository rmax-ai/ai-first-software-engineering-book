# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` around the newest long-form duplicate-count guard modes.
2. Add a dedicated adjacency assertion runner that checks paired uniqueness-guard predecessor index + 1 equals exact-once mode index.
3. Run the targeted smoke mode that validates this adjacency relationship.
4. Record execution and validation evidence in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_148/01-task.md`
- `state/feature_iterations/iter_148/02-plan.md`
- `state/feature_iterations/iter_148/03-execution.md`
- `state/feature_iterations/iter_148/04-validation.md`
- `state/feature_iterations/iter_148/05-risks-and-decisions.md`
- `state/feature_iterations/iter_148/06-next-iteration.md`
- `state/feature_iterations/iter_148/07-summary.md`
