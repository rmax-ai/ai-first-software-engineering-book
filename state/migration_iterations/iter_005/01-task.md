# Task

## Selected task title
Map Copilot SDK lifecycle failures to explicit `LLMClientError` stages in `state/llm_client.py`.

## Why this task now
`iter_004/06-next-iteration.md` recommended lifecycle failure mapping as the next smallest M2 hardening step for deterministic kernel error handling.

## Acceptance criteria
- SDK startup/session/send failures are wrapped with specific actionable `LLMClientError` messages.
- Error wrapping does not alter successful response behavior.
- Existing `mock` behavior remains unchanged.
