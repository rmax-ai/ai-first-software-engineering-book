# Plan

1. Inspect existing duplicate-count wrapper PASS message guard modes in `state/copilot_sdk_smoke_test.py` and follow the same AST-based source parsing pattern.
2. Add a new delimiter guard function that checks wrapper helper second-argument PASS message literals contain exactly one ` mode validates ` delimiter.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` near the literal/prefix/suffix guard entries with deterministic mode description text.
4. Run the targeted smoke command for the new mode and record the observed PASS output.
5. Write all seven iteration artifacts under `state/feature_iterations/iter_100/`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_100/01-task.md`
- `state/feature_iterations/iter_100/02-plan.md`
- `state/feature_iterations/iter_100/03-execution.md`
- `state/feature_iterations/iter_100/04-validation.md`
- `state/feature_iterations/iter_100/05-risks-and-decisions.md`
- `state/feature_iterations/iter_100/06-next-iteration.md`
- `state/feature_iterations/iter_100/07-summary.md`
