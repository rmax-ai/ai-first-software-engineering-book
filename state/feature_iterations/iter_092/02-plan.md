# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` for duplicate-count wrapper functions and mode-spec registration structure.
2. Add a new guard handler that:
   - Collects duplicate-count coverage-guard mode handlers from `TRACE_SUMMARY_MODE_SPECS`.
   - Uses `inspect.getsource(...)` to detect direct `_all_mode_specs()` usage.
   - Fails with wrapper names if regressions are found.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` near related usage-example guards.
4. Run the new smoke mode with `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-all-mode-specs-guard`.
5. Record execution, validation evidence, risks, and one next task.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_092/01-task.md`
- `state/feature_iterations/iter_092/02-plan.md`
- `state/feature_iterations/iter_092/03-execution.md`
- `state/feature_iterations/iter_092/04-validation.md`
- `state/feature_iterations/iter_092/05-risks-and-decisions.md`
- `state/feature_iterations/iter_092/06-next-iteration.md`
- `state/feature_iterations/iter_092/07-summary.md`
