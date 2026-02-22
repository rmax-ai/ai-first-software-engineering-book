# Plan

1. Add a new guard-mode function near existing duplicate-count wrapper helper guard checks in `state/copilot_sdk_smoke_test.py`.
2. Reuse existing AST parsing pattern over wrapper handlers to detect helper call nodes.
3. Fail if any wrapper has a helper call shape other than exactly two positional args with no keyword args.
4. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
5. Run the targeted smoke command and record output.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_102/01-task.md`
- `state/feature_iterations/iter_102/02-plan.md`
- `state/feature_iterations/iter_102/03-execution.md`
- `state/feature_iterations/iter_102/04-validation.md`
- `state/feature_iterations/iter_102/05-risks-and-decisions.md`
- `state/feature_iterations/iter_102/06-next-iteration.md`
- `state/feature_iterations/iter_102/07-summary.md`
