# Plan

1. Add a minimal HTTP fallback method in `state/llm_client.py`.
2. Wire `chat()` to call HTTP fallback only when SDK path returns unavailable.
3. Validate SDK stub path and HTTP fallback path with targeted commands.

## Expected files to change
- `state/llm_client.py`
