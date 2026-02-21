# Next Iteration Recommendation

## Recommended next task (exactly one)
Add a focused regression test for `session.error` propagation from the SDK adapter to `LLMClientError`.

## Why it is next
- M2 hardening also requires deterministic failure mapping; usage fallback is now covered, but explicit session error mapping still needs direct regression coverage.

## Acceptance criteria
- Stub returns a `session.error` event with a known message.
- Test asserts `LLMClient.chat(...)` raises `LLMClientError` containing that message.
- Test remains offline and deterministic.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/llm_client.py` (only if test exposes a gap)
