# Task

## Selected task title
Attempt live-provider smoke validation for non-mock `LLMClient` path.

## Why this task now
Migration plan still requires live-provider smoke coverage; this is the smallest remaining uncovered area.

## Acceptance criteria for this iteration
- Attempt at least one non-mock provider call via `LLMClient.chat(...)`.
- If call succeeds, record usage evidence.
- If blocked, capture exact reason and minimal unblock action.
