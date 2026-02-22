# Plan

1. Inspect existing duplicate-count helper guard wrappers around the newest adjacency/uniqueness sequence in `state/copilot_sdk_smoke_test.py`.
2. Add one new `...uniqueness...guard` wrapper function that counts the newest adjacency mode in `TRACE_SUMMARY_MODE_SPECS` and asserts it is exactly one.
3. Register the new mode tuple in `TRACE_SUMMARY_MODE_SPECS` directly next to the related adjacency and uniqueness guard modes.
4. Execute the targeted smoke command for the new mode and collect output evidence.
5. Record results, risks, decisions, and one concrete follow-up task in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_123/01-task.md`
- `state/feature_iterations/iter_123/02-plan.md`
- `state/feature_iterations/iter_123/03-execution.md`
- `state/feature_iterations/iter_123/04-validation.md`
- `state/feature_iterations/iter_123/05-risks-and-decisions.md`
- `state/feature_iterations/iter_123/06-next-iteration.md`
- `state/feature_iterations/iter_123/07-summary.md`
