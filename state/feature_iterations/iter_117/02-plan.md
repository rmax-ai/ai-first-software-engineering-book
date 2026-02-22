# Plan

1. Update `state/copilot_sdk_smoke_test.py` with a new mode handler that checks adjacency between `...-uniqueness-guard` and `usage-examples-mode-set-coverage-guard`.
2. Add the new mode to `TRACE_SUMMARY_MODE_SPECS` without changing public interfaces.
3. Execute the targeted smoke mode command and capture output for validation artifacts.
4. Document execution, validation, risks, next task, and summary in `state/feature_iterations/iter_117/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_117/01-task.md`
- `state/feature_iterations/iter_117/02-plan.md`
- `state/feature_iterations/iter_117/03-execution.md`
- `state/feature_iterations/iter_117/04-validation.md`
- `state/feature_iterations/iter_117/05-risks-and-decisions.md`
- `state/feature_iterations/iter_117/06-next-iteration.md`
- `state/feature_iterations/iter_117/07-summary.md`
