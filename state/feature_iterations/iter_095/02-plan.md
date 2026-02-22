# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one wrapper-source guard mode that inspects helper call AST argument shape.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so parser choices and generated usage examples include it deterministically.
3. Execute the targeted smoke command for the new mode and capture evidence.
4. Write all seven iteration artifacts under `state/feature_iterations/iter_095/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_095/01-task.md`
- `state/feature_iterations/iter_095/02-plan.md`
- `state/feature_iterations/iter_095/03-execution.md`
- `state/feature_iterations/iter_095/04-validation.md`
- `state/feature_iterations/iter_095/05-risks-and-decisions.md`
- `state/feature_iterations/iter_095/06-next-iteration.md`
- `state/feature_iterations/iter_095/07-summary.md`
