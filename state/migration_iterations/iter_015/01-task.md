# Task

## Selected task title
Harden Copilot SDK adapter reliability and bounded kernel shutdown behavior.

## Why this task now
The SDK migration code path existed, but shutdown failures could still override successful kernel runs, and usage extraction from `assistant.usage` events was not robust across event shapes.

## Acceptance criteria for this iteration
- `state/llm_client.py` aggregates usage from `assistant.usage` events and normalizes SDK event type variants.
- Kernel finalizer does not fail an otherwise successful run when close/stop errors occur.
- Focused smoke checks pass for SDK adapter behavior.
