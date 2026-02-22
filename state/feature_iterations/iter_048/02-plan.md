# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` near the latest duplicate-count mode coverage guard handlers.
2. Add one new handler for the 18-suffix mode that asserts presence in argparse `--mode` choices and generated usage examples.
3. Add one new `TRACE_SUMMARY_MODE_SPECS` tuple entry wiring the new mode name to the new handler.
4. Run only the two targeted smoke commands specified by acceptance criteria.
5. Record evidence and decisions in `state/feature_iterations/iter_048/03-07`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_048/01-task.md`
- `state/feature_iterations/iter_048/02-plan.md`
- `state/feature_iterations/iter_048/03-execution.md`
- `state/feature_iterations/iter_048/04-validation.md`
- `state/feature_iterations/iter_048/05-risks-and-decisions.md`
- `state/feature_iterations/iter_048/06-next-iteration.md`
- `state/feature_iterations/iter_048/07-summary.md`
