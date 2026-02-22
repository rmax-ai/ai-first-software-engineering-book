# Plan

1. Inspect existing guard patterns in `state/copilot_sdk_smoke_test.py` for doc/help/choices coverage.
2. Implement `usage-examples-coverage-guard` mode that:
   - builds expected non-`stub` command lines from mode metadata
   - compares them against generated `_usage_doc_lines(...)` command lines
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` to expose it in docs/parser choices.
4. Run targeted smoke validations for `stub` and the new guard mode.
5. Record evidence and hand off a single next task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_021/01-task.md`
- `state/feature_iterations/iter_021/02-plan.md`
- `state/feature_iterations/iter_021/03-execution.md`
- `state/feature_iterations/iter_021/04-validation.md`
- `state/feature_iterations/iter_021/05-risks-and-decisions.md`
- `state/feature_iterations/iter_021/06-next-iteration.md`
- `state/feature_iterations/iter_021/07-summary.md`
