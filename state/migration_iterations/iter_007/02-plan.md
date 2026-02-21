# Plan

## Step-by-step plan for this single task
1. Update `LLMClient.close()` to attempt `session.destroy()` before client stop.
2. Preserve current stop-first and force-stop-on-failure flow.
3. Surface session teardown failures with explicit `LLMClientError` details.
4. Run targeted validation for syntax and shutdown behavior.

## Files expected to change
- `state/llm_client.py`
