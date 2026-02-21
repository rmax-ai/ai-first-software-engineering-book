# Plan

1. Update `state/llm_client.py` `close()` to prefer `stop()` success path.
2. Add fallback to `force_stop()` only when stop path fails.
3. Keep no-op behavior when no SDK client exists.
4. Run targeted syntax and shutdown-behavior checks.

## Files expected to change
- `state/llm_client.py`
- `state/migration_iterations/iter_006/*.md`
