# Plan

1. Inspect `run_usage_examples_duplicates_guard_mode` in `state/copilot_sdk_smoke_test.py` and confirm it still computes duplicate checks without reusing the expected-mode helper.
2. Apply a minimal refactor so the guard reuses `_expected_non_stub_mode_names(...)` and reports duplicate mode names deterministically.
3. Execute the two required smoke commands for `usage-examples-duplicates-guard` and `usage-examples-coverage-guard`.
4. Record implementation details, validation evidence, risks, and next handoff in `state/feature_iterations/iter_027/*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_027/01-task.md`
- `state/feature_iterations/iter_027/02-plan.md`
- `state/feature_iterations/iter_027/03-execution.md`
- `state/feature_iterations/iter_027/04-validation.md`
- `state/feature_iterations/iter_027/05-risks-and-decisions.md`
- `state/feature_iterations/iter_027/06-next-iteration.md`
- `state/feature_iterations/iter_027/07-summary.md`
