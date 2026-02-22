# Next iteration recommendation

## Task
Implement deterministic loop-step trace event emission in `state/kernel.py` with smoke-test coverage in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
Trace observability is the highest-leverage foundation; later role-IO and eval enhancements depend on stable, structured kernel telemetry.

## Acceptance criteria
- `state/kernel.py` emits bounded structured trace events for each major loop stage (plan, change, evaluate, decide).
- Failures include explicit reason codes and preserve existing guardrail behavior.
- `state/copilot_sdk_uv_smoke.py` adds/updates tests proving trace-event presence, ordering, and bounded payload constraints.
- Validation includes `uv run python state/copilot_sdk_uv_smoke.py` with passing results for affected checks.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
