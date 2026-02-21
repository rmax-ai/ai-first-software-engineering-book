# Next Iteration

## Recommended next task
Start M2 cleanup by removing legacy HTTP fallback reliance for Copilot provider in `state/llm_client.py` so network providers use SDK-only behavior.

## Why it is next
Fallback mapping coverage is now complete; the migration plan’s open decision says legacy HTTP fallback should be removed after M2 stabilization.

## Acceptance criteria
- `LLMClient.chat()` no longer routes Copilot calls to `_chat_copilot_http(...)`.
- When SDK is unavailable for `provider="copilot"`, a clear `LLMClientError` is raised without HTTP fallback.
- `state/copilot_sdk_smoke_test.py --mode stub` continues to pass.

## Expected files to touch
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py`

