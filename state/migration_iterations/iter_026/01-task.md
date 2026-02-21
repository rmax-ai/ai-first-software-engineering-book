# Task

## Selected task title
Remove legacy HTTP fallback routing for Copilot provider and require Copilot SDK availability.

## Why this task now
`iter_025/06-next-iteration.md` marked this as the next M2 cleanup step after fallback mapping coverage was completed.

## Acceptance criteria
- `LLMClient.chat()` no longer routes Copilot requests to `_chat_copilot_http(...)`.
- Missing SDK for `provider="copilot"` raises clear `LLMClientError` without HTTP fallback.
- `python state/copilot_sdk_smoke_test.py --mode stub` passes.
