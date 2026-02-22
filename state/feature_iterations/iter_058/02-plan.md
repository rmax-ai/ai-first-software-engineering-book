# Plan

1. Extend `state/copilot_sdk_uv_smoke.py` fixture builder to support a malformed non-object payload variant.
2. Add a dedicated smoke mode that enables the new fixture variant while keeping existing malformed-key mode unchanged.
3. Run three targeted smoke commands:
   - `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`
   - `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase`
   - `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload`
4. Write all seven iteration artifacts with outcomes and one concrete next task.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_058/01-task.md`
- `state/feature_iterations/iter_058/02-plan.md`
- `state/feature_iterations/iter_058/03-execution.md`
- `state/feature_iterations/iter_058/04-validation.md`
- `state/feature_iterations/iter_058/05-risks-and-decisions.md`
- `state/feature_iterations/iter_058/06-next-iteration.md`
- `state/feature_iterations/iter_058/07-summary.md`
