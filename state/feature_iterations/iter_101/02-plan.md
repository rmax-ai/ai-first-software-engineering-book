# Plan

1. Reuse existing duplicate-count wrapper guard patterns to implement a new AST-based helper-argument literal-only guard mode in `state/copilot_sdk_smoke_test.py`.
2. Scope the AST rule to helper-call args and fail if any arg is an `ast.JoinedStr` (f-string) or string-concatenation `ast.BinOp(Add)`.
3. Add mode registration entry in `TRACE_SUMMARY_MODE_SPECS` next to existing duplicate-count wrapper guard modes.
4. Execute the targeted smoke command for the new mode and record PASS output in validation artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_101/01-task.md`
- `state/feature_iterations/iter_101/02-plan.md`
- `state/feature_iterations/iter_101/03-execution.md`
- `state/feature_iterations/iter_101/04-validation.md`
- `state/feature_iterations/iter_101/05-risks-and-decisions.md`
- `state/feature_iterations/iter_101/06-next-iteration.md`
- `state/feature_iterations/iter_101/07-summary.md`
