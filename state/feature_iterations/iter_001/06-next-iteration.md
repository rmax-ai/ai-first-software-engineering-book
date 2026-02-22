# Next Iteration Recommendation

## Recommended task
Implement deterministic trace-summary normalization and validation in the harness execution path.

## Why this is next
- It delivers immediate observability value in `state/kernel.py`.
- It is a small, testable vertical slice touching planned surfaces without broad refactors.
- It enables concrete smoke/eval assertions for later backlog items.

## Acceptance criteria
1. `state/kernel.py` exposes/uses a helper that normalizes phase trace summary entries and rejects malformed shapes.
2. `state/copilot_sdk_uv_smoke.py` includes one deterministic mode that fails on malformed trace-summary payload and passes on valid payload.
3. One eval contract under `evals/` is updated or added to assert the expected trace-summary signal shape.
4. Validation evidence is recorded in `state/feature_iterations/iter_002/04-validation.md` with executed commands and outputs.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/*.yaml` (single focused contract file)
- `state/feature_iterations/iter_002/01-task.md` through `07-summary.md`
