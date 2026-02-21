# Plan

1. Update `state/llm_client.py` so nested-loop contexts run SDK coroutines on a dedicated worker loop.
2. Ensure worker loop lifecycle is tied to `LLMClient.close()` cleanup.
3. Run targeted smoke checks plus a focused nested-loop bridge verification.

## Files expected to change
- `state/llm_client.py`
