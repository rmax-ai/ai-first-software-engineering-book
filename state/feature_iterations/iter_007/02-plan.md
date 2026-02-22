# Plan

1. Add one deterministic malformed-container mode in `state/copilot_sdk_smoke_test.py` that feeds invalid `chapters` shape into `_get_latest_trace_summary`.
2. Wire the mode into usage text, `--mode` choices, and mode dispatch.
3. Run targeted validation for compile and trace-summary modes.
4. Record execution, validation, risks, and next-step guidance in this iteration folder.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_007/01-task.md`
- `state/feature_iterations/iter_007/02-plan.md`
- `state/feature_iterations/iter_007/03-execution.md`
- `state/feature_iterations/iter_007/04-validation.md`
- `state/feature_iterations/iter_007/05-risks-and-decisions.md`
- `state/feature_iterations/iter_007/06-next-iteration.md`
- `state/feature_iterations/iter_007/07-summary.md`
