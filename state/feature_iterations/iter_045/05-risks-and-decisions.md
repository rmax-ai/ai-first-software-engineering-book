# Risks and decisions

## Risks discovered
- Mode names and handlers are intentionally repetitive and long; manual extension risks copy/paste mismatches between function names, target mode strings, and mode-spec registration.

## Decisions made and trade-offs
- Followed the established deterministic pattern exactly and added only one new suffix level to keep the diff minimal and predictable.
- Deferred any refactor/deduplication because this iteration requires only one smallest unfinished task.

## Intentionally deferred
- Refactoring repetitive guard functions into generated/table-driven helpers.
