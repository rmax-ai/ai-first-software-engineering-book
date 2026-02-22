# Plan

1. Add one dedicated long-form adjacency-order runner in `state/copilot_sdk_smoke_test.py` comparing indices of the newest `...-adjacency-order-guard-uniqueness-guard` mode and prior `...-adjacency-order-guard` mode.
2. Keep assertions deterministic by verifying both modes exist and enforcing `new_index + 1 == prior_index`.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` mode mapped to the new runner, placed directly before the existing uniqueness assertion mode.
4. Run targeted smoke validation for the new mode and capture PASS output.
5. Record execution, validation, risks, next-task handoff, and summary in `state/feature_iterations/iter_142/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_142/01-task.md`
- `state/feature_iterations/iter_142/02-plan.md`
- `state/feature_iterations/iter_142/03-execution.md`
- `state/feature_iterations/iter_142/04-validation.md`
- `state/feature_iterations/iter_142/05-risks-and-decisions.md`
- `state/feature_iterations/iter_142/06-next-iteration.md`
- `state/feature_iterations/iter_142/07-summary.md`
