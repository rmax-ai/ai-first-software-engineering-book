# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` around the latest duplicate-count mode coverage guard handler and mode table tail.
2. Add one new handler for the 20-suffix mode that asserts presence in argparse `--mode` choices and generated usage examples.
3. Add one `TRACE_SUMMARY_MODE_SPECS` tuple entry wiring the new mode name to the new handler.
4. Run the two targeted smoke commands from acceptance criteria.
5. Record commands, outputs, risks, and next-task handoff in `state/feature_iterations/iter_050/03-07`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_050/01-task.md`
- `state/feature_iterations/iter_050/02-plan.md`
- `state/feature_iterations/iter_050/03-execution.md`
- `state/feature_iterations/iter_050/04-validation.md`
- `state/feature_iterations/iter_050/05-risks-and-decisions.md`
- `state/feature_iterations/iter_050/06-next-iteration.md`
- `state/feature_iterations/iter_050/07-summary.md`
