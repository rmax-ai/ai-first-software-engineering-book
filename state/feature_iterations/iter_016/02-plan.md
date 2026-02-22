# Plan
1. Add a `BASE_MODE_SPECS` table in `state/copilot_sdk_smoke_test.py` with base mode name, handler, and help description.
2. Build one combined mode list/help string/handler map from base + shutdown + trace-summary mode specs.
3. Replace hard-coded base mode branch chain with table-driven dispatch.
4. Run targeted smoke modes plus Python syntax validation.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_016/01-task.md`
- `state/feature_iterations/iter_016/02-plan.md`
- `state/feature_iterations/iter_016/03-execution.md`
- `state/feature_iterations/iter_016/04-validation.md`
- `state/feature_iterations/iter_016/05-risks-and-decisions.md`
- `state/feature_iterations/iter_016/06-next-iteration.md`
- `state/feature_iterations/iter_016/07-summary.md`
