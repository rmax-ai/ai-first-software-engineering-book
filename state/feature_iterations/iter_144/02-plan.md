# Plan

1. Inspect adjacent long-form wrapper helper runners in `state/copilot_sdk_smoke_test.py` and reuse the existing assertion pattern.
2. Add one new runner that checks index ordering between:
   - `...-uniqueness-guard-adjacency-order-guard-uniqueness-guard`
   - `...-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`
3. Register one new mode entry in `TRACE_SUMMARY_MODE_SPECS` mapped to the new runner.
4. Run the targeted smoke mode and record results.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_144/01-task.md`
- `state/feature_iterations/iter_144/02-plan.md`
- `state/feature_iterations/iter_144/03-execution.md`
- `state/feature_iterations/iter_144/04-validation.md`
- `state/feature_iterations/iter_144/05-risks-and-decisions.md`
- `state/feature_iterations/iter_144/06-next-iteration.md`
- `state/feature_iterations/iter_144/07-summary.md`
