# Plan

1. Inspect `state/kernel.py` metrics persistence logic to identify minimal insertion point for trace summary.
2. Add an additive `trace_summary` object to each metrics history entry without removing existing keys.
3. Run targeted verification (`py_compile`) for edited module.
4. Record execution, validation, risks, and one next task in iteration artifacts.

## Files expected to change
- `state/kernel.py`
- `state/feature_iterations/iter_003/01-task.md`
- `state/feature_iterations/iter_003/02-plan.md`
- `state/feature_iterations/iter_003/03-execution.md`
- `state/feature_iterations/iter_003/04-validation.md`
- `state/feature_iterations/iter_003/05-risks-and-decisions.md`
- `state/feature_iterations/iter_003/06-next-iteration.md`
- `state/feature_iterations/iter_003/07-summary.md`
