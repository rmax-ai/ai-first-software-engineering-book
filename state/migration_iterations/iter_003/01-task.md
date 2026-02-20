# Task

## Selected task title
Introduce a guarded Copilot SDK adapter path in `state/llm_client.py` for non-mock providers.

## Why this task now
`iter_002` identified this as the next smallest migration step after kernel lifecycle teardown was completed.

## Acceptance criteria
- `LLMClient.chat(...)` public signature/return shape remains unchanged.
- `mock` provider behavior remains deterministic and unchanged.
- Non-mock providers attempt a guarded SDK path with legacy HTTP fallback retained.
