# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with one new deterministic mode handler for the eight-suffix `coverage-guard` chain.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so argparse mode choices and generated usage examples include it.
3. Run the two required smoke checks from the prior iteration handoff.
4. Record execution, validation evidence, and next-step guidance in `state/feature_iterations/iter_038/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_038/01-task.md`
- `state/feature_iterations/iter_038/02-plan.md`
- `state/feature_iterations/iter_038/03-execution.md`
- `state/feature_iterations/iter_038/04-validation.md`
- `state/feature_iterations/iter_038/05-risks-and-decisions.md`
- `state/feature_iterations/iter_038/06-next-iteration.md`
- `state/feature_iterations/iter_038/07-summary.md`
