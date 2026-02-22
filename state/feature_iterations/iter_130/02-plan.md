# Plan

1. Inspect the latest `TRACE_SUMMARY_MODE_SPECS` ordering around the newest `...order-uniqueness-guard` and `...order-guard` modes in `state/copilot_sdk_smoke_test.py`.
2. Add one focused guard function that asserts the newest uniqueness guard is immediately before its corresponding adjacency-order guard.
3. Register the new `...order-uniqueness-order-guard` mode with deterministic description text.
4. Run the targeted smoke command for the new mode and capture PASS evidence.
5. Write all seven required artifacts in `state/feature_iterations/iter_130/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_130/01-task.md`
- `state/feature_iterations/iter_130/02-plan.md`
- `state/feature_iterations/iter_130/03-execution.md`
- `state/feature_iterations/iter_130/04-validation.md`
- `state/feature_iterations/iter_130/05-risks-and-decisions.md`
- `state/feature_iterations/iter_130/06-next-iteration.md`
- `state/feature_iterations/iter_130/07-summary.md`
