# Plan

1. Add a small helper in `state/copilot_sdk_smoke_test.py` that encapsulates wrapper setup (`all_mode_specs`, shared assertion call, PASS output).
2. Migrate exactly two wrappers:
   - `run_usage_examples_duplicate_count_mode_coverage_guard_mode`
   - `run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_mode`
3. Keep PASS strings unchanged to preserve deterministic output.
4. Run the two required smoke modes from acceptance criteria.
5. Record execution, validation evidence, risks, and one next scoped task in iter_080 artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_080/01-task.md`
- `state/feature_iterations/iter_080/02-plan.md`
- `state/feature_iterations/iter_080/03-execution.md`
- `state/feature_iterations/iter_080/04-validation.md`
- `state/feature_iterations/iter_080/05-risks-and-decisions.md`
- `state/feature_iterations/iter_080/06-next-iteration.md`
- `state/feature_iterations/iter_080/07-summary.md`
