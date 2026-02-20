# Next Iteration Recommendation

## Recommended next task
Introduce an SDK-backed adapter path in `state/llm_client.py` behind provider selection while preserving legacy HTTP behavior as fallback.

## Why this is next
Lifecycle cleanup is now wired; the next smallest migration step is routing non-mock providers through a Copilot SDK adapter path without breaking existing interfaces.

## Acceptance criteria
- `LLMClient.chat(...)` keeps the same public signature and return shape.
- `mock` provider remains deterministic and unchanged.
- A guarded SDK path exists for non-mock providers, with legacy HTTP fallback retained.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_003/*.md`
