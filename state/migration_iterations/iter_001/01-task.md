# Task

## Selected task title
Add a compatibility shutdown hook to `state/llm_client.py` (`LLMClient.close()`).

## Why this task now
This is the smallest unfinished migration prerequisite for kernel-managed SDK/client lifecycle cleanup.

## Acceptance criteria
- `LLMClient` exposes a `close()` method without changing existing `chat(...)` behavior.
- Existing providers (`copilot`, `copilot`, `mock`) remain unaffected.
