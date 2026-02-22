# Next iteration recommendation

## Task
Implement deterministic trace-summary observability in `state/kernel.py` with smoke coverage updates.

## Why this is next
- It is the highest-leverage foundation for later eval hardening.
- It converts the planning output into measurable harness behavior.

## Acceptance criteria
- `state/kernel.py` emits stable trace-summary fields for key phases and guardrail decisions.
- `state/copilot_sdk_uv_smoke.py` adds at least one focused mode validating trace-summary output.
- Validation evidence includes `uv run python state/copilot_sdk_uv_smoke.py` for the new mode(s).
- Iteration artifacts record commands, outcomes, and any residual risk.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md` ... `07-summary.md`
