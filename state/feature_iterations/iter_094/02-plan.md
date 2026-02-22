# Plan

1. Reuse the existing wrapper-source introspection pattern in `state/copilot_sdk_smoke_test.py`.
2. Add a new guard mode that enumerates duplicate-count coverage-guard wrappers and checks helper call count equals exactly one.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so parser choices and generated usage examples include it.
4. Run targeted smoke validation for the new mode and record evidence in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_094/01-task.md`
- `state/feature_iterations/iter_094/02-plan.md`
- `state/feature_iterations/iter_094/03-execution.md`
- `state/feature_iterations/iter_094/04-validation.md`
- `state/feature_iterations/iter_094/05-risks-and-decisions.md`
- `state/feature_iterations/iter_094/06-next-iteration.md`
- `state/feature_iterations/iter_094/07-summary.md`
