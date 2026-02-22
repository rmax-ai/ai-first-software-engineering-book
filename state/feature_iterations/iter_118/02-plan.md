# Plan

1. Add a new smoke-mode function in `state/copilot_sdk_smoke_test.py` that counts occurrences of `...-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS` and asserts exactly one.
2. Add the corresponding mode registration tuple in `TRACE_SUMMARY_MODE_SPECS` near existing adjacent uniqueness/adjacency guard modes.
3. Run the targeted smoke test mode command and record the outcome.
4. Write iteration artifacts documenting execution, validation, risks, and the next smallest task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_118/01-task.md`
- `state/feature_iterations/iter_118/02-plan.md`
- `state/feature_iterations/iter_118/03-execution.md`
- `state/feature_iterations/iter_118/04-validation.md`
- `state/feature_iterations/iter_118/05-risks-and-decisions.md`
- `state/feature_iterations/iter_118/06-next-iteration.md`
- `state/feature_iterations/iter_118/07-summary.md`
