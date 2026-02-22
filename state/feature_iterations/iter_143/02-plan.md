# Plan

1. Inspect the newest long-form duplicate-count guard modes in `state/copilot_sdk_smoke_test.py` to find the existing adjacency-order guard and nearby registration order.
2. Add one new runner function that counts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` and asserts it appears exactly once.
3. Add one new entry in `TRACE_SUMMARY_MODE_SPECS` for the new uniqueness-count runner.
4. Execute the targeted smoke mode command and capture the PASS output.
5. Write iteration artifacts under `state/feature_iterations/iter_143/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_143/01-task.md`
- `state/feature_iterations/iter_143/02-plan.md`
- `state/feature_iterations/iter_143/03-execution.md`
- `state/feature_iterations/iter_143/04-validation.md`
- `state/feature_iterations/iter_143/05-risks-and-decisions.md`
- `state/feature_iterations/iter_143/06-next-iteration.md`
- `state/feature_iterations/iter_143/07-summary.md`
