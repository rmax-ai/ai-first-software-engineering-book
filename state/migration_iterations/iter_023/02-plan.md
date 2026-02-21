# Plan

1. Add a new smoke mode in `state/copilot_sdk_smoke_test.py` that forces fallback `URLError`.
2. Assert `LLMClientError` message includes `HTTP fallback connection failed`.
3. Run targeted fallback smoke checks and compile validation.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
