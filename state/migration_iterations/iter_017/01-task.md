# Task

## Selected task
Add a focused regression test for `send_and_wait` usage fallback behavior in the SDK adapter.

## Why this task now
- `iter_016/06-next-iteration.md` explicitly recommended this as the next smallest unfinished migration task.
- It validates M2 hardening for token accounting when message events omit usage fields.

## Acceptance criteria
- Simulate `assistant.message` without embedded usage plus separate `assistant.usage` event(s).
- Assert `LLMResponse.usage.prompt_tokens` and `completion_tokens` are recovered correctly.
- Keep the test offline and deterministic.
