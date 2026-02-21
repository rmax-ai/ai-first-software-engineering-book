# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py`
- `python state/copilot_sdk_smoke_test.py --mode stub`
- Inline Python harness with local HTTP server + patched `copilot` import failure to exercise fallback.

## Files changed
- `state/llm_client.py`

## Rationale
- Added `_chat_copilot_http(...)` to preserve M0 fallback behavior.
- Updated `chat(...)` to prefer SDK and only use HTTP fallback when SDK is unavailable.
- Kept public interfaces unchanged.
