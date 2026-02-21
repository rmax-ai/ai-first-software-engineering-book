# Next Iteration Recommendation

## Recommended next task
Map SDK/session lifecycle failures to clearer `LLMClientError` categories in `state/llm_client.py`.

## Why it is next
Usage extraction is now hardened; focused failure mapping is the next smallest M2 hardening step for deterministic kernel error handling.

## Concrete acceptance criteria
- SDK startup/session/send failures are wrapped with specific actionable `LLMClientError` messages.
- Error wrapping does not alter successful response behavior.
- Existing `mock` behavior remains unchanged.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_005/*.md`
