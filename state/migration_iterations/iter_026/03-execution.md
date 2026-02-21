# Execution

## Commands/tools run
- `view state/llm_client.py`
- `view state/copilot_sdk_smoke_test.py`
- `apply_patch state/llm_client.py`
- `apply_patch state/copilot_sdk_smoke_test.py`
- `python state/copilot_sdk_smoke_test.py --mode stub`
- `python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`

## Files changed
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Removed Copilot HTTP fallback routing from `LLMClient.chat()` so Copilot provider is SDK-only.
- Replaced SDK import/capability fallback with explicit, actionable SDK-required errors.
- Updated smoke test mode wiring to validate SDK-unavailable behavior directly.
