# Plan

1. Add a new adjacency-order smoke runner in `state/copilot_sdk_smoke_test.py` near the newest long-form duplicate-count wrapper helpers.
2. Reuse the existing two long-form mode strings and assert index adjacency (`new + 1 == prior`).
3. Register one new `TRACE_SUMMARY_MODE_SPECS` entry that maps to the new runner.
4. Run the targeted smoke mode command and record PASS output.
5. Document execution, validation, risks/decisions, next task, and summary in `state/feature_iterations/iter_140/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_140/01-task.md`
- `state/feature_iterations/iter_140/02-plan.md`
- `state/feature_iterations/iter_140/03-execution.md`
- `state/feature_iterations/iter_140/04-validation.md`
- `state/feature_iterations/iter_140/05-risks-and-decisions.md`
- `state/feature_iterations/iter_140/06-next-iteration.md`
- `state/feature_iterations/iter_140/07-summary.md`
