# Next Iteration Recommendation

## Task
Add deterministic trace-summary logging hooks in `state/kernel.py` and validate with smoke coverage.

## Why next
- It is the smallest implementation step that improves observability while preserving current orchestration behavior.
- It directly enables measurable validation through existing smoke and eval flows.

## Acceptance criteria
- `state/kernel.py` emits a stable trace-summary payload (shape-defined keys, deterministic ordering).
- `state/copilot_sdk_uv_smoke.py` includes one targeted mode asserting the trace-summary payload shape.
- Validation run: `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` passes.
- Iteration artifacts document results and any impacted eval contracts under `evals/`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
