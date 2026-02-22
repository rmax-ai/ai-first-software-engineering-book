# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one new mode: `trace-summary-missing-chapter-guard`.
2. Wire the mode through usage docs, mode descriptions, CLI `choices`, help text, and dispatch logic.
3. Use a deterministic fixture where `chapters` has no requested chapter key and assert the expected guard message.
4. Run targeted smoke commands to verify the new mode and adjacent trace-summary behavior.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_011/01-task.md`
- `state/feature_iterations/iter_011/02-plan.md`
- `state/feature_iterations/iter_011/03-execution.md`
- `state/feature_iterations/iter_011/04-validation.md`
- `state/feature_iterations/iter_011/05-risks-and-decisions.md`
- `state/feature_iterations/iter_011/06-next-iteration.md`
- `state/feature_iterations/iter_011/07-summary.md`
