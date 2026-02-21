# Task

## Selected task title
Harden SDK usage extraction in `state/llm_client.py` to aggregate `assistant.usage` event data when direct usage is absent.

## Why this task now
`iter_003` explicitly recommended usage aggregation hardening as the smallest next migration step for resource accounting.

## Acceptance criteria
- Usage extraction supports direct response usage and event-list usage shapes.
- Missing usage data falls back safely to zeroed `LLMUsage`.
- Existing mock and legacy HTTP provider paths remain unchanged.
