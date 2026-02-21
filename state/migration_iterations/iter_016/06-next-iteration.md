# Next Iteration Recommendation

## Recommended next task (exactly one)
Add a focused regression test for `send_and_wait` usage fallback behavior in the SDK adapter.

## Why this is next
- The code path was hardened, but there is no explicit test proving event-based usage recovery when message usage is absent.

## Acceptance criteria
- Test simulates `assistant.message` without usage plus separate `assistant.usage` event(s).
- Test asserts `LLMResponse.usage.prompt_tokens` and `completion_tokens` are recovered correctly.
- Test runs offline and deterministic.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/llm_client.py` (only if test reveals gaps)
