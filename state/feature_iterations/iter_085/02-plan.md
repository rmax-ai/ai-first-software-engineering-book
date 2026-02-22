# Plan

1. Locate the next two non-migrated duplicate-count coverage-guard wrappers after the 10-guard migrated wrapper.
2. Replace each inline parser/assert/print body with `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.
3. Preserve wrapper names and PASS strings exactly.
4. Run the two smoke modes required by the prior iteration handoff.
5. Record execution details, validation evidence, risks, and one recommended next task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_085/01-task.md`
- `state/feature_iterations/iter_085/02-plan.md`
- `state/feature_iterations/iter_085/03-execution.md`
- `state/feature_iterations/iter_085/04-validation.md`
- `state/feature_iterations/iter_085/05-risks-and-decisions.md`
- `state/feature_iterations/iter_085/06-next-iteration.md`
- `state/feature_iterations/iter_085/07-summary.md`
