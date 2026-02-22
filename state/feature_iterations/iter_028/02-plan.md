# Plan

1. Inspect `run_usage_examples_duplicates_guard_mode` in `state/copilot_sdk_smoke_test.py` and capture the current duplicate-diagnostic format.
2. Apply a minimal diff so duplicate failures include deterministic `{mode_name: count}` output ordered by `_expected_non_stub_mode_names(...)`.
3. Run required smoke validations for `usage-examples-duplicates-guard` and `usage-examples-order-guard`.
4. Document execution, validation, risks, and one next task in `state/feature_iterations/iter_028/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_028/01-task.md`
- `state/feature_iterations/iter_028/02-plan.md`
- `state/feature_iterations/iter_028/03-execution.md`
- `state/feature_iterations/iter_028/04-validation.md`
- `state/feature_iterations/iter_028/05-risks-and-decisions.md`
- `state/feature_iterations/iter_028/06-next-iteration.md`
- `state/feature_iterations/iter_028/07-summary.md`
