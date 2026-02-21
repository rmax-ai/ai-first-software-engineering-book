# Plan

1. Update `state/llm_client.py` to make Copilot calls SDK-only.
2. Update `state/copilot_sdk_smoke_test.py` to validate SDK-unavailable failure behavior.
3. Run targeted smoke checks for `stub` and `sdk-unavailable` modes.

## Expected files to change
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py`
