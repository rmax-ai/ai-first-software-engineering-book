# Recommended next iteration

## Next task (exactly one)
Add deterministic trace-summary observability scaffolding in `state/kernel.py` and assert it in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- It is the smallest implementation slice from the new plan.
- It establishes measurable signals required for later eval alignment.

## Acceptance criteria
- `state/kernel.py` emits a stable, parseable trace-summary payload for a representative run path.
- `state/copilot_sdk_uv_smoke.py` includes a targeted mode that validates the trace-summary payload structure.
- Validation evidence includes running `uv run python state/copilot_sdk_uv_smoke.py` with the new mode and recording observed output.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
