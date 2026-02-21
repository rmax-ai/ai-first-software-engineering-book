# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a `fallback-timeout` mode.
2. Force HTTP fallback by patching Copilot import and `urlopen` to raise `TimeoutError`.
3. Assert `LLMClientError` contains `HTTP fallback timed out`.
4. Wire the new mode into CLI usage/help/dispatch.
5. Validate with `py_compile` and targeted smoke execution.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
