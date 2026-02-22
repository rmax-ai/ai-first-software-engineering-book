# Next iteration recommendation

## Task
Implement deterministic phase-trace validation helpers in `state/kernel.py` and cover them with focused smoke assertions in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- It is the smallest executable slice from the plan that improves observability and regression detection without broad refactoring.
- It directly strengthens validation signals consumed by existing eval workflows and iteration artifacts.

## Acceptance criteria
1. `state/kernel.py` exposes/refactors pure helper logic that validates required `phase_trace` payload shape and required phase presence.
2. Kernel writes explicit failure details for malformed/missing phase traces while preserving current public kernel CLI behavior.
3. `state/copilot_sdk_uv_smoke.py` adds/updates at least one targeted mode that fails on malformed or missing phase traces and passes on valid traces.
4. Validation evidence includes `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary` plus the new/updated failure mode.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- Optional: `state/.smoke_fixtures/trace_summary/*` (if fixture updates are required)
