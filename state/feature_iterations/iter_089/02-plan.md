# Plan

1. Update exactly two remaining duplicate-count coverage-guard wrapper functions in `state/copilot_sdk_smoke_test.py` to delegate to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.
2. Preserve wrapper names, target mode names, and PASS strings verbatim to avoid behavior drift.
3. Run the two required `uv run python state/copilot_sdk_smoke_test.py --mode ...` commands for the touched wrappers.
4. Record execution evidence, validation results, risks, and next step in `state/feature_iterations/iter_089/0{3..7}-*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_089/01-task.md`
- `state/feature_iterations/iter_089/02-plan.md`
- `state/feature_iterations/iter_089/03-execution.md`
- `state/feature_iterations/iter_089/04-validation.md`
- `state/feature_iterations/iter_089/05-risks-and-decisions.md`
- `state/feature_iterations/iter_089/06-next-iteration.md`
- `state/feature_iterations/iter_089/07-summary.md`
