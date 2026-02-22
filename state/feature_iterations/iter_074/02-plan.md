# Plan

1. Add a new composite parity guard function near existing parity guard modes in `state/copilot_sdk_smoke_test.py`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so argparse choices and generated usage examples include it deterministically.
3. Run focused smoke checks for the new mode and existing mode/doc coverage guards.
4. Document execution, validation, risks, and one next task across the iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_074/01-task.md`
- `state/feature_iterations/iter_074/02-plan.md`
- `state/feature_iterations/iter_074/03-execution.md`
- `state/feature_iterations/iter_074/04-validation.md`
- `state/feature_iterations/iter_074/05-risks-and-decisions.md`
- `state/feature_iterations/iter_074/06-next-iteration.md`
- `state/feature_iterations/iter_074/07-summary.md`
