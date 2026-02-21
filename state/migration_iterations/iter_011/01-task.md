# Task

## Selected task title
Validate SDK usage/resource accounting normalization across response/event shapes.

## Why this task now
Migration plan still requires resource-accounting assurance; this task is unblocked and directly verifies token normalization semantics.

## Acceptance criteria for this iteration
- Validate direct usage dict shape extraction.
- Validate `assistant.usage` event-list extraction.
- Validate missing usage fallback to zero.
- Confirm resulting usage values are integers and non-negative.
