# Recommended next task

## Task
Implement deterministic trace-summary schema validation in `state/kernel.py`.

## Why this is next
- It provides the highest leverage observability improvement while staying narrow and testable.
- It creates concrete outputs that later role-template and eval-gate changes can build on.

## Acceptance criteria
- Add a focused helper in `state/kernel.py` that validates the trace summary payload shape before persistence.
- Emit actionable errors when required trace fields are missing or malformed; do not silently coerce invalid structures.
- Add/extend deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py` proving both valid and invalid trace-summary paths.
- Verification run includes at least one targeted smoke command and records expected pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/metrics.json` (only if trace validation adds a new stable signal)
