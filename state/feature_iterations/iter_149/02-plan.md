# Plan

1. Inspect the newest long-form adjacency-order guard assertions in `state/copilot_sdk_smoke_test.py`.
2. Add one alias runner that re-checks the exact-once count for the newest long-form adjacency-order guard mode.
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for that alias mode.
4. Publish the new iteration by updating the feature-iteration index surfaces and writing the seven `iter_149` artifacts.
5. Run targeted validation for the new smoke mode plus the existing governance ledger check.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/README.md`
- `state/feature_iterations/iter_149/01-task.md`
- `state/feature_iterations/iter_149/02-plan.md`
- `state/feature_iterations/iter_149/03-execution.md`
- `state/feature_iterations/iter_149/04-validation.md`
- `state/feature_iterations/iter_149/05-risks-and-decisions.md`
- `state/feature_iterations/iter_149/06-next-iteration.md`
- `state/feature_iterations/iter_149/07-summary.md`
- `README.md`
- `docs/index.md`
