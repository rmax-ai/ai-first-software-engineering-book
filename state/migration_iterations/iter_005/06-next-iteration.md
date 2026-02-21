# Next Iteration Recommendation

## Recommended next task
Harden SDK shutdown in `LLMClient.close()` to use bounded `stop()` with `force_stop()` fallback only on failure.

## Why it is next
M2 still calls for robust shutdown behavior; this is the next smallest reliability step after lifecycle failure mapping.

## Concrete acceptance criteria
- `close()` attempts `stop()` first and only falls back to `force_stop()` when stop fails.
- Shutdown errors are surfaced as actionable `LLMClientError` messages.
- No behavior change for runs that never initialized SDK client/session.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_006/*.md`
