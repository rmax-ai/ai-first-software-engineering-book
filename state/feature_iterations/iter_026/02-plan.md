# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` for duplicated expected non-`stub` mode-name comprehensions.
2. Add a private helper that derives expected non-`stub` mode names from provided mode specs.
3. Replace duplicated comprehensions in the three targeted usage-example guard modes with the helper.
4. Run the three required smoke commands.
5. Record execution, validation, risks, and next step in `iter_026` artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_026/01-task.md`
- `state/feature_iterations/iter_026/02-plan.md`
- `state/feature_iterations/iter_026/03-execution.md`
- `state/feature_iterations/iter_026/04-validation.md`
- `state/feature_iterations/iter_026/05-risks-and-decisions.md`
- `state/feature_iterations/iter_026/06-next-iteration.md`
- `state/feature_iterations/iter_026/07-summary.md`
