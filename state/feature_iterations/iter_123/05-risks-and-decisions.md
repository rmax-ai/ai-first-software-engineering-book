# Risks and decisions

## Risks discovered
- Long mode strings are error-prone and can drift by one suffix; this can silently weaken deterministic coverage if not guarded.

## Decisions made and trade-offs
- Reused the existing wrapper/assertion pattern to minimize diff scope and keep naming consistent with prior modes.
- Added only one new guard mode as requested instead of batching additional cleanups to avoid unrelated churn.

## Anything intentionally deferred
- Additional deduplication/refactor of long mode-name constants remains deferred to keep this iteration single-task and low risk.
