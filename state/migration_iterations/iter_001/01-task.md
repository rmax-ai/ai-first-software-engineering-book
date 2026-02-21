# Task

## Selected task
Stabilize Copilot SDK usage accounting when `send_and_wait` returns an `assistant.message` event without embedded usage tokens.

## Why this task now
- It is a small unfinished migration hardening item from M2 ("usage extraction fallback when usage events are absent").
- It preserves current kernel interfaces while improving token accounting reliability.

## Acceptance criteria
- `state/llm_client.py` falls back to session events for usage when message-level usage is missing.
- Existing smoke test still passes.
