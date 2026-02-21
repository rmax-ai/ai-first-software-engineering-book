# Next Iteration Recommendation

## Recommended next task
Reset SDK client/session references after successful shutdown in `LLMClient.close()` to prevent stale object reuse across repeated runs.

## Why it is next
M2 still emphasizes avoiding orphaned runtime state; explicit teardown now exists, and clearing cached handles is the next smallest reliability hardening step.

## Concrete acceptance criteria
- `close()` sets `_sdk_client` and `_sdk_session` to `None` after successful shutdown paths.
- Error paths preserve actionable `LLMClientError` details without swallowing failures.
- Existing mock/provider chat behavior remains unchanged.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_008/*.md`
