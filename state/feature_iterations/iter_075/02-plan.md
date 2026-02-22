# Plan

1. Introduce one shared helper returning the two parity cleanup mode names.
2. Replace repeated inline tuples in parity guard mode functions with calls to the helper.
3. Run the two required smoke modes to verify behavior parity and mode registration coverage.
4. Record execution, validation, risks, next step, and summary in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_075/01-task.md`
- `state/feature_iterations/iter_075/02-plan.md`
- `state/feature_iterations/iter_075/03-execution.md`
- `state/feature_iterations/iter_075/04-validation.md`
- `state/feature_iterations/iter_075/05-risks-and-decisions.md`
- `state/feature_iterations/iter_075/06-next-iteration.md`
- `state/feature_iterations/iter_075/07-summary.md`
