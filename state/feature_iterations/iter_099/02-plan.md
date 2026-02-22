# Plan

1. Inspect existing duplicate-count wrapper guard modes in `state/copilot_sdk_smoke_test.py` to mirror AST-based pattern checks.
2. Add a new guard function that validates wrapper helper second-argument PASS message suffixes follow `duplicate-count ... mode coverage`.
3. Register the mode in `TRACE_SUMMARY_MODE_SPECS` beside the existing PASS message literal/prefix guard entries.
4. Run the targeted smoke command for the new mode and record observed PASS output.
5. Write iteration artifacts with execution details, validation evidence, risks, and one next task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_099/01-task.md`
- `state/feature_iterations/iter_099/02-plan.md`
- `state/feature_iterations/iter_099/03-execution.md`
- `state/feature_iterations/iter_099/04-validation.md`
- `state/feature_iterations/iter_099/05-risks-and-decisions.md`
- `state/feature_iterations/iter_099/06-next-iteration.md`
- `state/feature_iterations/iter_099/07-summary.md`
