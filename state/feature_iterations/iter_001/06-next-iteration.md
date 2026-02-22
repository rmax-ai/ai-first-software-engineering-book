# Recommended next task
Implement deterministic kernel trace summary enrichment and validation guards.

## Why this is next
- It is the smallest implementation slice that unlocks observability and makes later smoke/eval wiring concrete.
- It directly exercises the highest-priority harness file (`state/kernel.py`) while keeping scope contained.

## Acceptance criteria
1. `state/kernel.py` emits a stable, structured trace summary payload that includes run id, chapter id, and per-stage status counts.
2. `state/copilot_sdk_uv_smoke.py` adds deterministic assertions for the new trace summary shape.
3. Validation command `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-shape-guard` passes.
4. Iteration artifacts document command output and any eval impact references.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
