# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one new mode: `trace-summary-chapter-metrics-shape-guard`.
2. Wire the mode through usage docs, mode descriptions, CLI `choices`, help text, and dispatch logic.
3. Use a deterministic fixture where `chapters["01-paradigm-shift"]` is a list to trigger chapter-metrics shape assertion.
4. Run targeted smoke commands to verify the new mode and ensure existing trace-summary behavior remains unchanged.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_012/01-task.md`
- `state/feature_iterations/iter_012/02-plan.md`
- `state/feature_iterations/iter_012/03-execution.md`
- `state/feature_iterations/iter_012/04-validation.md`
- `state/feature_iterations/iter_012/05-risks-and-decisions.md`
- `state/feature_iterations/iter_012/06-next-iteration.md`
- `state/feature_iterations/iter_012/07-summary.md`
