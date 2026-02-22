# Recommended Next Iteration Task

## Task
Implement deterministic trace-summary observability in `state/kernel.py` and expose aligned role I/O scaffolds in `state/role_io_templates.py`.

## Why this is next
- It is the highest-value harness feature from this plan and unblocks meaningful smoke/eval assertions.
- It creates concrete output signals that later eval updates can measure.

## Acceptance criteria
1. Kernel emits a stable trace-summary structure for each loop with bounded fields.
2. Role I/O template helpers include explicit sections matching the trace-summary contract.
3. Add/extend targeted deterministic checks in `state/copilot_sdk_uv_smoke.py` that assert the new structure.
4. Validation evidence includes `uv run python state/copilot_sdk_uv_smoke.py` with relevant mode(s) and observed pass/fail.

## Expected files to touch
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
