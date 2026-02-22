# Plan

1. Inspect existing usage-example guard helpers in `state/copilot_sdk_smoke_test.py` and identify where to add a parity-specific guard mode.
2. Implement one new deterministic guard function that parses generated usage-example lines and asserts single occurrences for:
   - `trace-summary-fixture-root-cleanup-parity`
   - `trace-summary-fixture-cleanup-parity`
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` without changing existing parity execution handlers.
4. Run targeted smoke validations for the new mode and mode/doc coverage guards.
5. Write iteration artifacts with evidence and one concrete next task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_070/01-task.md`
- `state/feature_iterations/iter_070/02-plan.md`
- `state/feature_iterations/iter_070/03-execution.md`
- `state/feature_iterations/iter_070/04-validation.md`
- `state/feature_iterations/iter_070/05-risks-and-decisions.md`
- `state/feature_iterations/iter_070/06-next-iteration.md`
- `state/feature_iterations/iter_070/07-summary.md`
