# Plan

1. Inspect the newest duplicate-count guard helper functions around the latest adjacency-order and uniqueness-adjacency modes in `state/copilot_sdk_smoke_test.py`.
2. Add one new uniqueness-count guard mode function that counts occurrences of the `...order-uniqueness-adjacency-guard` mode and asserts exactly one occurrence.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording matching current conventions.
4. Run the targeted smoke command for the new mode and record evidence.
5. Write all seven iteration artifacts under `state/feature_iterations/iter_127/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_127/01-task.md`
- `state/feature_iterations/iter_127/02-plan.md`
- `state/feature_iterations/iter_127/03-execution.md`
- `state/feature_iterations/iter_127/04-validation.md`
- `state/feature_iterations/iter_127/05-risks-and-decisions.md`
- `state/feature_iterations/iter_127/06-next-iteration.md`
- `state/feature_iterations/iter_127/07-summary.md`
