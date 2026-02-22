# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one new mode: `trace-summary-empty-history-guard`.
2. Route the mode through usage docs, mode descriptions, CLI `choices`, help text, and dispatch logic.
3. Implement a deterministic fixture with `history: []` and assert the expected guard message.
4. Run targeted smoke commands for the new mode plus adjacent guard modes to verify no regressions.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_010/01-task.md`
- `state/feature_iterations/iter_010/02-plan.md`
- `state/feature_iterations/iter_010/03-execution.md`
- `state/feature_iterations/iter_010/04-validation.md`
- `state/feature_iterations/iter_010/05-risks-and-decisions.md`
- `state/feature_iterations/iter_010/06-next-iteration.md`
- `state/feature_iterations/iter_010/07-summary.md`
