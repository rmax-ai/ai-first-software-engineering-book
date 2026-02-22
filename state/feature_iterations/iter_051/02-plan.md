# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` for the latest duplicate-count mode-coverage guard handler and mode registration entry.
2. Add one new guard handler for the next suffix depth by mirroring the existing deterministic assertion structure.
3. Append one matching mode spec tuple entry in `TRACE_SUMMARY_MODE_SPECS`.
4. Run the two targeted smoke commands from acceptance criteria.
5. Record execution, validation evidence, decisions, and next task in `state/feature_iterations/iter_051/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_051/01-task.md`
- `state/feature_iterations/iter_051/02-plan.md`
- `state/feature_iterations/iter_051/03-execution.md`
- `state/feature_iterations/iter_051/04-validation.md`
- `state/feature_iterations/iter_051/05-risks-and-decisions.md`
- `state/feature_iterations/iter_051/06-next-iteration.md`
- `state/feature_iterations/iter_051/07-summary.md`
