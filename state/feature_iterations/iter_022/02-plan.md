# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` usage-example guard structure and reuse its command-line extraction logic.
2. Add `usage-examples-duplicates-guard` mode that asserts extracted generated non-`stub` usage command lines are unique.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so parser choices/help/doc generation include it without special wiring.
4. Run targeted smoke validations for `stub` and `usage-examples-duplicates-guard`.
5. Record execution evidence, risks, and one next recommended task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_022/01-task.md`
- `state/feature_iterations/iter_022/02-plan.md`
- `state/feature_iterations/iter_022/03-execution.md`
- `state/feature_iterations/iter_022/04-validation.md`
- `state/feature_iterations/iter_022/05-risks-and-decisions.md`
- `state/feature_iterations/iter_022/06-next-iteration.md`
- `state/feature_iterations/iter_022/07-summary.md`
