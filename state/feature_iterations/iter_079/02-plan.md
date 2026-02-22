# Plan

1. Read the latest iteration guidance and inspect `state/copilot_sdk_smoke_test.py` wrapper implementations.
2. Replace repeated parser/usage assertions in remaining duplicate-count coverage-guard wrappers with `_assert_mode_in_parser_and_usage_examples(all_mode_specs, target_mode_name)`.
3. Confirm PASS strings remain unchanged while reviewing the diff.
4. Run the two targeted smoke modes from acceptance criteria.
5. Record execution, validation evidence, risks, and one scoped next task in iter_079 artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_079/01-task.md`
- `state/feature_iterations/iter_079/02-plan.md`
- `state/feature_iterations/iter_079/03-execution.md`
- `state/feature_iterations/iter_079/04-validation.md`
- `state/feature_iterations/iter_079/05-risks-and-decisions.md`
- `state/feature_iterations/iter_079/06-next-iteration.md`
- `state/feature_iterations/iter_079/07-summary.md`
