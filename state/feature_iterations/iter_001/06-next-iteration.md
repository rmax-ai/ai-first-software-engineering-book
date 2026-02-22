# Next Iteration Task

## Recommended task
Implement deterministic trace stage metrics in `state/kernel.py`.

## Why this is next
- It delivers the highest-value observability feature from this plan.
- It creates concrete signals that smoke tests and eval contracts can validate.

## Acceptance criteria
- Kernel trace summaries include per-stage counters and stable shape guards.
- `state/copilot_sdk_uv_smoke.py` adds targeted checks for the new trace fields.
- Validation run documents `uv run python state/copilot_sdk_uv_smoke.py --mode ...` results.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
