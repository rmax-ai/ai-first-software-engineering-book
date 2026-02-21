# Plan

1. Extend the stub Copilot session in `state/copilot_sdk_smoke_test.py` to expose `send_and_wait()` and `get_messages()` fallback events.
2. Keep existing smoke assertions and verify they now pass through the fallback path.
3. Run `uv run python state/copilot_sdk_smoke_test.py`.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
