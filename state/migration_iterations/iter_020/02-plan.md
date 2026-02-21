# Plan

1. Extend smoke test CLI with a new fallback error mode.
2. Run a local deterministic HTTP server that returns status 500 payload.
3. Force Copilot SDK import failure so the fallback path is exercised.
4. Assert raised `LLMClientError` includes `HTTP fallback failed (500)`.
5. Run targeted compile + smoke validations.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
