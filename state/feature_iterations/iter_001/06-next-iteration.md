# Recommended Next Task

## Task
Implement kernel trace-envelope improvements in `state/kernel.py` with deterministic visibility fields.

## Why this is next
- `state/kernel.py` is the highest-impact integration point for observability and deterministic controls.
- Downstream role-IO and smoke updates depend on stable kernel trace shape.

## Acceptance criteria
- Add explicit trace fields for loop budget usage, step outcomes, and failure reasons.
- Preserve existing kernel public behavior while enriching emitted trace data.
- Add/adjust targeted tests for trace shape and determinism.
- Validate with `uv run python state/copilot_sdk_uv_smoke.py` on relevant modes.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- Relevant `state/` test files for kernel trace assertions
