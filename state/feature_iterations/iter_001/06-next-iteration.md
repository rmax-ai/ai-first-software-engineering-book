# Recommended Next Iteration Task

## Next task
Add deterministic trace-summary telemetry helper(s) in `state/kernel.py` and validate coverage in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
The plan identified observability and deterministic execution signals as the highest-value baseline needed before broader harness refactors.

## Acceptance criteria
- `state/kernel.py` gains a focused helper path that emits stable trace-summary fields for iteration outcomes.
- `state/copilot_sdk_uv_smoke.py` adds/updates one deterministic scenario that asserts the new trace-summary shape.
- Validation includes `uv run python state/copilot_sdk_uv_smoke.py` with recorded pass/fail evidence.
- Iteration docs under the next `state/feature_iterations/iter_XXX/` capture command output and risk notes.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md`
- `state/feature_iterations/iter_002/02-plan.md`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
- `state/feature_iterations/iter_002/05-risks-and-decisions.md`
- `state/feature_iterations/iter_002/06-next-iteration.md`
- `state/feature_iterations/iter_002/07-summary.md`
