# Plan
1. Add a `SHUTDOWN_MODE_SPECS` table in `state/copilot_sdk_smoke_test.py` with mode name, handler, and help description.
2. Derive shutdown `--mode` choices and help fragment from the same table.
3. Replace shutdown mode branch chain with table-driven dispatch.
4. Run targeted smoke modes plus Python syntax validation.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_015/01-task.md`
- `state/feature_iterations/iter_015/02-plan.md`
- `state/feature_iterations/iter_015/03-execution.md`
- `state/feature_iterations/iter_015/04-validation.md`
- `state/feature_iterations/iter_015/05-risks-and-decisions.md`
- `state/feature_iterations/iter_015/06-next-iteration.md`
- `state/feature_iterations/iter_015/07-summary.md`
