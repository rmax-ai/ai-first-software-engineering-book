# Plan

1. Add `run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_mode` in `state/copilot_sdk_smoke_test.py`.
2. Reuse `_build_parser(...)` and `_usage_doc_lines(...)` to assert the target mode appears in parser choices and generated usage mode names.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with a deterministic description.
4. Run the two required smoke commands and capture PASS evidence.
5. Write all `iter_031` artifacts with execution, validation, risk, and handoff details.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_031/01-task.md`
- `state/feature_iterations/iter_031/02-plan.md`
- `state/feature_iterations/iter_031/03-execution.md`
- `state/feature_iterations/iter_031/04-validation.md`
- `state/feature_iterations/iter_031/05-risks-and-decisions.md`
- `state/feature_iterations/iter_031/06-next-iteration.md`
- `state/feature_iterations/iter_031/07-summary.md`
