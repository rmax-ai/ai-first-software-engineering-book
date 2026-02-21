# Execution

## Commands/tools run
- Edited `state/copilot_sdk_smoke_test.py` via patch.
- Ran:
  - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
  - `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
  - `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added a deterministic `bootstrap-failure` mode that forces `_ensure_sdk_thread_loop` to raise `LLMClientError` with bootstrap context and asserts that context.
- Updated script usage docs, mode descriptions, argparse choices, and dispatch logic.
