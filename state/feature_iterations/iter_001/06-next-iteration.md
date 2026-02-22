# Recommended next task

## Task
Implement deterministic trace-summary emission in `state/kernel.py` for key loop stages.

## Why this is next
- It is the smallest concrete feature from the plan that improves observability without changing public interfaces.
- It unlocks stronger smoke and eval assertions in subsequent iterations.

## Acceptance criteria
1. Add a minimal, deterministic trace-summary helper and wire it into the kernel loop at clearly defined checkpoints.
2. Ensure trace output remains stable across identical runs.
3. Validate with a targeted harness command (for example `uv run python state/copilot_sdk_uv_smoke.py --mode <targeted-mode>`) and record results.
4. Update iteration artifacts with evidence and any follow-up risk notes.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
