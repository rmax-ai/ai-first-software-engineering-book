# Plan

1. Inspect `state/llm_client.py` normalization path for `send_and_wait` results.
2. Add a minimal fallback: if `assistant.message` lacks usage, read `session.get_messages()` and derive usage from `assistant.usage` events.
3. Run targeted validation via `uv run python state/copilot_sdk_smoke_test.py`.

## Expected files
- `state/llm_client.py`
