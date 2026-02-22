# Plan

1. Reuse the existing duplicate-count wrapper AST-guard pattern to add a second-argument PASS message literal check.
2. Register the new mode adjacent to existing duplicate-count wrapper guard modes in `TRACE_SUMMARY_MODE_SPECS`.
3. Execute targeted smoke validation for the new mode and the base duplicate-count coverage guard mode.
4. Document execution evidence, validation outcomes, risks, and the next single task recommendation.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_097/01-task.md`
- `state/feature_iterations/iter_097/02-plan.md`
- `state/feature_iterations/iter_097/03-execution.md`
- `state/feature_iterations/iter_097/04-validation.md`
- `state/feature_iterations/iter_097/05-risks-and-decisions.md`
- `state/feature_iterations/iter_097/06-next-iteration.md`
- `state/feature_iterations/iter_097/07-summary.md`
