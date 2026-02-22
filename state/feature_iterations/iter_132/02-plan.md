# Plan

1. Inspect the latest `...order-uniqueness-order-uniqueness-guard` and `...order-uniqueness-order-guard` function/spec anchors in `state/copilot_sdk_smoke_test.py`.
2. Add one adjacency-order assertion function for that pair and keep naming/wording consistent with existing guard wrappers.
3. Register one new `...order-uniqueness-order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS` without changing unrelated entries.
4. Run the targeted smoke mode command and confirm PASS.
5. Record execution details, validation evidence, risks, and one follow-up task in iter_132 artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_132/01-task.md`
- `state/feature_iterations/iter_132/02-plan.md`
- `state/feature_iterations/iter_132/03-execution.md`
- `state/feature_iterations/iter_132/04-validation.md`
- `state/feature_iterations/iter_132/05-risks-and-decisions.md`
- `state/feature_iterations/iter_132/06-next-iteration.md`
- `state/feature_iterations/iter_132/07-summary.md`
