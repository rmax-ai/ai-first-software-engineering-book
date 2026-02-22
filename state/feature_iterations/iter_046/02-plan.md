# Plan

1. Add one new deterministic guard function in `state/copilot_sdk_smoke_test.py` by extending the existing duplicate-count mode-coverage progression with one additional `-coverage-guard` suffix.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with the existing naming/description pattern.
3. Run the two targeted smoke validations from the acceptance criteria.
4. Record execution evidence and outcomes in iteration artifacts.

## Files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_046/03-execution.md`
- `state/feature_iterations/iter_046/04-validation.md`
- `state/feature_iterations/iter_046/05-risks-and-decisions.md`
- `state/feature_iterations/iter_046/06-next-iteration.md`
- `state/feature_iterations/iter_046/07-summary.md`
