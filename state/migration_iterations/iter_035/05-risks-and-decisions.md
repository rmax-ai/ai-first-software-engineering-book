# Risks and Decisions

## Risks discovered
- The helper now centralizes preconditions, so any future warmup behavior changes affect all four shutdown modes at once.

## Decisions made and trade-offs
- Kept one setup helper and one teardown helper instead of broader refactoring to stay minimal and focused on requested duplication.
- Kept all existing mode assertions untouched to preserve deterministic behavior and output contracts.

## Intentionally deferred
- Additional cleanup deduplication for other modes (`stub`, `sdk-unavailable`, `bootstrap-failure`) remains out of scope for this single-task iteration.
