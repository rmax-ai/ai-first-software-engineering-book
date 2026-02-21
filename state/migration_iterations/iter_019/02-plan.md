# Plan

1. Extend smoke test modes to add a fallback-specific mode.
2. Spin up a local stdlib HTTP server returning deterministic chat completion payload.
3. Force SDK import unavailability and assert fallback content/usage/request payload.
4. Run targeted smoke validation (`stub` + `fallback`).

## Expected files to change
- `state/copilot_sdk_smoke_test.py`
