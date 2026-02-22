# Risks and Decisions

## Risks discovered
- The `TRACE_SUMMARY_MODE_SPECS` sequence is tightly coupled to many order/adjacency guards, so accidental reorderings can break targeted checks.

## Decisions made and trade-offs
- Added only the requested uniqueness guard with minimal diff instead of broader list cleanup to avoid changing unrelated ordering contracts.
- Kept deterministic PASS wording consistent with existing guard-mode conventions.

## Anything intentionally deferred
- Deferred additional order normalization in `TRACE_SUMMARY_MODE_SPECS`; not required for this single-task iteration.
