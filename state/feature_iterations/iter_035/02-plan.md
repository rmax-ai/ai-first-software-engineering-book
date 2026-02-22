# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a new deterministic mode handler for the five-suffix `coverage-guard` chain.
2. Register the new mode in `DETERMINISTIC_MODE_SPECS` so argparse mode choices and generated usage examples include it.
3. Run the two required smoke checks from the prior iteration handoff.
4. Record execution, validation evidence, and next-step guidance in `state/feature_iterations/iter_035/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_035/01-task.md`
- `state/feature_iterations/iter_035/02-plan.md`
- `state/feature_iterations/iter_035/03-execution.md`
- `state/feature_iterations/iter_035/04-validation.md`
- `state/feature_iterations/iter_035/05-risks-and-decisions.md`
- `state/feature_iterations/iter_035/06-next-iteration.md`
- `state/feature_iterations/iter_035/07-summary.md`
