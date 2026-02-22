# Plan

1. Inspect the duplicate-count guard chain in `state/copilot_sdk_smoke_test.py`.
2. Add one new guard handler that checks parser choices and usage-example coverage for `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`.
3. Register the handler in `TRACE_SUMMARY_MODE_SPECS` with a deterministic description string.
4. Run the two required smoke commands.
5. Write iteration artifacts with execution and validation evidence.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_032/01-task.md`
- `state/feature_iterations/iter_032/02-plan.md`
- `state/feature_iterations/iter_032/03-execution.md`
- `state/feature_iterations/iter_032/04-validation.md`
- `state/feature_iterations/iter_032/05-risks-and-decisions.md`
- `state/feature_iterations/iter_032/06-next-iteration.md`
- `state/feature_iterations/iter_032/07-summary.md`
