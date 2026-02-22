# Plan

1. Add a new parity adjacency guard function near existing parity guard modes in `state/copilot_sdk_smoke_test.py`.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` so it appears in argparse choices and generated usage examples.
3. Run focused smoke checks for the new mode and existing mode/doc coverage guards.
4. Document execution, validation, risks, and a single next task across the iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_073/03-execution.md`
- `state/feature_iterations/iter_073/04-validation.md`
- `state/feature_iterations/iter_073/05-risks-and-decisions.md`
- `state/feature_iterations/iter_073/06-next-iteration.md`
- `state/feature_iterations/iter_073/07-summary.md`
