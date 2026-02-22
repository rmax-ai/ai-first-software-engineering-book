# Plan

1. Add `run_usage_examples_duplicate_count_wrapper_helper_arg_order_guard_mode()` adjacent to existing duplicate-count wrapper helper guards in `state/copilot_sdk_smoke_test.py`.
2. Reuse existing AST parsing pattern to inspect `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` calls in wrapper handlers.
3. Assert canonical helper argument order and shape: first argument equals wrapper mode name literal; second argument starts with `PASS: <mode-name> mode validates`.
4. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
5. Run the targeted smoke command and record output in validation artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_103/01-task.md`
- `state/feature_iterations/iter_103/02-plan.md`
- `state/feature_iterations/iter_103/03-execution.md`
- `state/feature_iterations/iter_103/04-validation.md`
- `state/feature_iterations/iter_103/05-risks-and-decisions.md`
- `state/feature_iterations/iter_103/06-next-iteration.md`
- `state/feature_iterations/iter_103/07-summary.md`
