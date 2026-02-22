# Plan

1. Copy the most recent duplicate-count mode-coverage guard function in `state/copilot_sdk_smoke_test.py` and extend it by one `-coverage-guard` suffix.
2. Add the matching `TRACE_SUMMARY_MODE_SPECS` tuple entry so parser choices, help text, and dispatch include the new mode.
3. Run the two targeted smoke commands for argparse choice coverage and the new mode.
4. Record execution/validation evidence and decisions in `state/feature_iterations/iter_053/03-execution.md` through `07-summary.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_053/01-task.md`
- `state/feature_iterations/iter_053/02-plan.md`
- `state/feature_iterations/iter_053/03-execution.md`
- `state/feature_iterations/iter_053/04-validation.md`
- `state/feature_iterations/iter_053/05-risks-and-decisions.md`
- `state/feature_iterations/iter_053/06-next-iteration.md`
- `state/feature_iterations/iter_053/07-summary.md`
