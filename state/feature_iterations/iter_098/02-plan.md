# Plan

1. Inspect existing duplicate-count wrapper guard modes in `state/copilot_sdk_smoke_test.py` and follow the same AST-based helper-call parsing pattern.
2. Implement `run_usage_examples_duplicate_count_wrapper_pass_message_prefix_guard_mode()` to verify second helper-argument string literals use canonical PASS prefixes.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` near related duplicate-count wrapper guard entries.
4. Run targeted smoke validation commands for the new mode and baseline duplicate-count coverage mode.
5. Document execution, validation, risks, and next recommendation in `state/feature_iterations/iter_098/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_098/01-task.md`
- `state/feature_iterations/iter_098/02-plan.md`
- `state/feature_iterations/iter_098/03-execution.md`
- `state/feature_iterations/iter_098/04-validation.md`
- `state/feature_iterations/iter_098/05-risks-and-decisions.md`
- `state/feature_iterations/iter_098/06-next-iteration.md`
- `state/feature_iterations/iter_098/07-summary.md`
