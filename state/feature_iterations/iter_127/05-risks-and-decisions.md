# Risks and Decisions

## Risks discovered
- Long mode names remain typo-prone; a single segment mismatch would break the uniqueness assertion.

## Decisions made and trade-offs
- Followed the existing guard-wrapper pattern to keep the change minimal and deterministic.
- Kept validation targeted to the new mode to provide direct evidence with low runtime cost.

## Intentionally deferred
- Running the full smoke matrix was deferred because only one guard-mode registration path changed.
