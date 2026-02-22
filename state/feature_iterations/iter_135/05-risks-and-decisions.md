# Risks and decisions

## Risks discovered
- Extremely long mode identifiers are easy to mistype; a typo would make the guard ineffective.

## Decisions made and trade-offs
- Reused the existing explicit string-count guard pattern instead of refactoring shared helpers to keep the diff minimal and isolated.

## Anything intentionally deferred
- No refactor of long-name guard builders; deferred to keep this iteration scoped to one smallest unfinished task.
