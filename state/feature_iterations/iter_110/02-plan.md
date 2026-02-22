# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` guard-mode patterns near the existing uniqueness-order adjacency-order guards.
2. Implement one new guard function asserting the uniqueness-order adjacency-order uniqueness guard is immediately followed by `usage-examples-order-guard`.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic naming and description.
4. Run the targeted smoke mode command for this new guard.
5. Record execution, validation, risks, and next-step handoff in this iteration folder.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_110/01-task.md`
- `state/feature_iterations/iter_110/02-plan.md`
- `state/feature_iterations/iter_110/03-execution.md`
- `state/feature_iterations/iter_110/04-validation.md`
- `state/feature_iterations/iter_110/05-risks-and-decisions.md`
- `state/feature_iterations/iter_110/06-next-iteration.md`
- `state/feature_iterations/iter_110/07-summary.md`
