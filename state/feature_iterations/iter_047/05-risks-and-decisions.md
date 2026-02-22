# Risks and Decisions

## Risks discovered
- Mode names and handler names are now extremely long; manual edits are error-prone.
- Any mismatch between mode string, handler name, and registration tuple would break deterministic coverage unexpectedly.

## Decisions made and trade-offs
- Kept the established explicit-registration pattern for consistency and deterministic visibility.
- Limited scope to one additional suffix depth to satisfy “one smallest unfinished task.”

## Intentionally deferred
- Refactoring these repetitive guard handlers into generated/table-driven code.
