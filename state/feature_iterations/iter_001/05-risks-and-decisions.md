# Risks and Decisions

## Risks discovered
- Future harness updates may couple `state/kernel.py` behavior and smoke assertions more tightly, increasing maintenance overhead.
- Adding eval assertions too early may create brittle gates before trace schema stabilizes.

## Decisions and trade-offs
- Chose planning-only execution to honor seed-iteration requirements and avoid premature implementation churn.
- Kept planned coverage anchored to existing eval contracts instead of introducing new eval files immediately.

## Deferred intentionally
- Any concrete Python code changes in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
- Any eval YAML modifications until first implementation iteration validates baseline behavior deltas.
