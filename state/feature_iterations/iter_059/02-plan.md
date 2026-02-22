# Plan

1. Extend the trace-summary fixture builder in `state/copilot_sdk_uv_smoke.py` with a toggle that omits the `evaluation` phase entry.
2. Add `--mode trace-summary-missing-phase` that enables the new fixture variant and expects phase-trace validation failure.
3. Run four targeted smoke commands to prove the new mode and existing modes all behave as expected.
4. Write iteration artifacts with execution, validation evidence, risks, and one next task.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_059/01-task.md`
- `state/feature_iterations/iter_059/02-plan.md`
- `state/feature_iterations/iter_059/03-execution.md`
- `state/feature_iterations/iter_059/04-validation.md`
- `state/feature_iterations/iter_059/05-risks-and-decisions.md`
- `state/feature_iterations/iter_059/06-next-iteration.md`
- `state/feature_iterations/iter_059/07-summary.md`
