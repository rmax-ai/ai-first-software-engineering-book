# Plan

1. Add a new smoke handler in `state/copilot_sdk_smoke_test.py` that checks index adjacency between the long-form uniqueness guard mode and `usage-examples-order-guard`.
2. Register the new `...-uniqueness-adjacency-guard` mode in `TRACE_SUMMARY_MODE_SPECS` without breaking the adjacency it validates.
3. Run the targeted smoke mode command and record exact PASS output.
4. Document execution, validation, risks, and next step in `state/feature_iterations/iter_115/0*-*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_115/01-task.md`
- `state/feature_iterations/iter_115/02-plan.md`
- `state/feature_iterations/iter_115/03-execution.md`
- `state/feature_iterations/iter_115/04-validation.md`
- `state/feature_iterations/iter_115/05-risks-and-decisions.md`
- `state/feature_iterations/iter_115/06-next-iteration.md`
- `state/feature_iterations/iter_115/07-summary.md`
