# Plan

1. Add `_mode_action_for_parser(parser)` helper near parser helpers in `state/copilot_sdk_smoke_test.py`.
2. Replace duplicated `parser._actions` lookup blocks in parity cleanup guard modes with helper calls.
3. Execute the two required smoke modes and capture pass outputs.
4. Record execution, validation, risks, next task, and summary artifacts for iter_076.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_076/01-task.md`
- `state/feature_iterations/iter_076/02-plan.md`
- `state/feature_iterations/iter_076/03-execution.md`
- `state/feature_iterations/iter_076/04-validation.md`
- `state/feature_iterations/iter_076/05-risks-and-decisions.md`
- `state/feature_iterations/iter_076/06-next-iteration.md`
- `state/feature_iterations/iter_076/07-summary.md`
