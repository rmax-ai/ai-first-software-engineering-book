# Risks and Decisions

## Risks discovered
- Registry uniqueness guards rely on exact mode strings; accidental rename drift could invalidate coverage.

## Decisions made and trade-offs
- Added a narrow count assertion for the single mode instead of introducing generic registry helpers to keep this iteration minimal.
- Preserved the long mode naming convention because mode names are stable external smoke interfaces.

## Intentionally deferred
- Adjacency checks between the new uniqueness guard and neighboring modes were deferred to keep scope to one smallest unfinished task.
