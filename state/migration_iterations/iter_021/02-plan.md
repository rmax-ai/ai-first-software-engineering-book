# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a new `fallback-invalid-json` mode.
2. Force HTTP fallback by patching `importlib.import_module` for `copilot` import attempts.
3. Serve a deterministic non-JSON response and assert `LLMClientError` includes invalid JSON context.
4. Validate with `py_compile` and smoke modes (`stub`, `fallback`, `fallback-invalid-json`).

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
