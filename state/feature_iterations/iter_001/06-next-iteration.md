# Recommended next iteration task

## Task
Add deterministic phase-trace schema guards in the harness and smoke matrix.

## Why this is next
Trace schema stabilization in `state/kernel.py` and `state/copilot_sdk_uv_smoke.py` provides the safest foundation for subsequent role-template and eval contract changes.

## Acceptance criteria
- `state/kernel.py` emits explicit phase-trace fields for phase name, tool usage summary, and validation status.
- `state/copilot_sdk_uv_smoke.py` includes at least one deterministic mode that fails when the new trace fields are missing or malformed.
- Validation evidence includes `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` output and one targeted kernel run.
- Documentation in the new iteration artifacts maps changed trace fields to eval guard expectations.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
