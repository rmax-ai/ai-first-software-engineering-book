# Plan
1. Keep existing mode spec tables as single source of truth and add helpers to derive combined mode metadata once.
2. Generate usage and mode doc lines from the combined metadata and assign the module docstring from that output.
3. Keep argparse choice/help wiring on the same combined metadata helper.
4. Run required smoke modes and syntax validation.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_017/01-task.md`
- `state/feature_iterations/iter_017/02-plan.md`
- `state/feature_iterations/iter_017/03-execution.md`
- `state/feature_iterations/iter_017/04-validation.md`
- `state/feature_iterations/iter_017/05-risks-and-decisions.md`
- `state/feature_iterations/iter_017/06-next-iteration.md`
- `state/feature_iterations/iter_017/07-summary.md`
