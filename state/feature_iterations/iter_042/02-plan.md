# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one new deterministic handler that checks parser choices and generated usage examples for the next duplicate-count mode-coverage guard-chain mode.
2. Register the new mode/handler/description tuple in `TRACE_SUMMARY_MODE_SPECS` so argparse choices and generated usage examples include it.
3. Run the two targeted smoke commands from the prior handoff to verify acceptance criteria.
4. Record execution evidence, validation output, risks, and next task in the iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_042/01-task.md`
- `state/feature_iterations/iter_042/02-plan.md`
- `state/feature_iterations/iter_042/03-execution.md`
- `state/feature_iterations/iter_042/04-validation.md`
- `state/feature_iterations/iter_042/05-risks-and-decisions.md`
- `state/feature_iterations/iter_042/06-next-iteration.md`
- `state/feature_iterations/iter_042/07-summary.md`
