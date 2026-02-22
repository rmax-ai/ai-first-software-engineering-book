# Recommended next iteration task

## Task
Implement structured trace-summary guard events in `state/kernel.py` and cover them with a deterministic smoke mode.

## Why this is next
Trace visibility is the foundation for validating later role-IO and eval wiring changes; adding it first reduces debugging ambiguity across all following iterations.

## Acceptance criteria
- `state/kernel.py` emits stable, parseable trace-summary guard payloads for required chapter metrics.
- `state/copilot_sdk_uv_smoke.py` includes one deterministic mode asserting the new trace-summary payload shape.
- Validation evidence includes the exact `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` command and observed pass result.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
