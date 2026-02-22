# Plan

1. Add a new long-form uniqueness-count runner in `state/copilot_sdk_smoke_test.py` for the `...uniqueness-guard-adjacency-order-guard` mode.
2. Reuse the exact long-form mode string from existing registrations and assert `.count(...) == 1`.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for the new runner, placed before the existing adjacency-order guard mode.
4. Run targeted smoke validation for the new mode and capture the PASS output.
5. Record execution, validation, risks, next-task handoff, and summary in `state/feature_iterations/iter_141/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_141/01-task.md`
- `state/feature_iterations/iter_141/02-plan.md`
- `state/feature_iterations/iter_141/03-execution.md`
- `state/feature_iterations/iter_141/04-validation.md`
- `state/feature_iterations/iter_141/05-risks-and-decisions.md`
- `state/feature_iterations/iter_141/06-next-iteration.md`
- `state/feature_iterations/iter_141/07-summary.md`
