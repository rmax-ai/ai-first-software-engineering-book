# Plan

1. Add shared trace-summary key-validation helpers in `state/copilot_sdk_smoke_test.py`.
2. Add `trace-summary` mode with a deterministic passing fixture.
3. Add `trace-summary-missing-key` mode with a deterministic missing-key fixture.
4. Wire both modes into CLI mode choices and dispatcher.
5. Run targeted verification commands for syntax and both new modes.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_005/01-task.md`
- `state/feature_iterations/iter_005/02-plan.md`
- `state/feature_iterations/iter_005/03-execution.md`
- `state/feature_iterations/iter_005/04-validation.md`
- `state/feature_iterations/iter_005/05-risks-and-decisions.md`
- `state/feature_iterations/iter_005/06-next-iteration.md`
- `state/feature_iterations/iter_005/07-summary.md`
