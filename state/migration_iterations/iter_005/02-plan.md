# Plan

1. Update `state/llm_client.py` SDK path to tag failures by lifecycle stage (options/client/start/session/send).
2. Preserve existing control flow and public `LLMClient.chat(...)` interface.
3. Run targeted validation for syntax and staged failure messages.

## Files expected to change
- `state/llm_client.py`
- `state/migration_iterations/iter_005/*.md`
