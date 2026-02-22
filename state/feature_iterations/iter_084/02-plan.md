# Plan

1. Locate the next two non-migrated duplicate-count coverage-guard wrappers immediately after the most recently migrated block.
2. Replace their inline parser/assert/print bodies with `_run_usage_examples_duplicate_count_mode_coverage_guard(...)` calls.
3. Preserve both wrapper names and PASS strings exactly.
4. Run the two smoke modes requested by prior iteration guidance.
5. Record execution, validation evidence, risks, and one next recommended task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_084/01-task.md`
- `state/feature_iterations/iter_084/02-plan.md`
- `state/feature_iterations/iter_084/03-execution.md`
- `state/feature_iterations/iter_084/04-validation.md`
- `state/feature_iterations/iter_084/05-risks-and-decisions.md`
- `state/feature_iterations/iter_084/06-next-iteration.md`
- `state/feature_iterations/iter_084/07-summary.md`

