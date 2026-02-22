# Recommended next task

## Task
Implement deterministic trace-summary observability scaffolding in `state/kernel.py`.

## Why this is next
- It is the smallest high-leverage implementation from the seed plan and unlocks clearer validation for later harness changes.

## Acceptance criteria
- Add a minimal, deterministic trace-summary helper path in `state/kernel.py` without changing public CLI behavior.
- Ensure emitted trace data is stable for identical inputs and bounded in size.
- Add/adjust targeted verification in `state/copilot_sdk_uv_smoke.py` for the new trace-summary signal.
- Run `uv run python state/copilot_sdk_uv_smoke.py` (or targeted mode) and record result evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
