# Recommended next iteration task

## Task
Implement deterministic phase-trace summary enrichment in `state/kernel.py` and validate it with smoke coverage.

## Why this is next
- It is the highest-leverage feature slice from the seed plan and improves observability without changing public interfaces.
- It provides a concrete anchor for pairing feature work with tests and eval-aligned validation.

## Acceptance criteria
- Add minimal kernel logic to emit richer, deterministic phase-trace summary fields.
- Add/adjust targeted smoke checks in `state/copilot_sdk_uv_smoke.py` proving success and malformed-trace failure paths.
- Document verification with `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary` and at least one malformed mode.
- Ensure no governance file mutations and no unrelated refactors.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*.md`
