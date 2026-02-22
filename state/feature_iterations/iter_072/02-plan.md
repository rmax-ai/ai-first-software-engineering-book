# Plan

1. Inspect existing parity cleanup guard helpers in `state/copilot_sdk_smoke_test.py` and mirror the deterministic assertion style.
2. Implement one new mode that reads argparse `--mode` choices and asserts each parity cleanup mode name appears exactly once.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS`.
4. Run targeted smoke validations for the new mode and relevant coverage guards.
5. Document execution, validation evidence, risks/decisions, and one next task in this iteration folder.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_072/01-task.md`
- `state/feature_iterations/iter_072/02-plan.md`
- `state/feature_iterations/iter_072/03-execution.md`
- `state/feature_iterations/iter_072/04-validation.md`
- `state/feature_iterations/iter_072/05-risks-and-decisions.md`
- `state/feature_iterations/iter_072/06-next-iteration.md`
- `state/feature_iterations/iter_072/07-summary.md`
