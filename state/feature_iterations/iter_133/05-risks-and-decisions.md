# Risks and decisions

## Risks discovered
- Extremely long mode identifiers are easy to mistype, which can silently miswire guard coverage.

## Decisions made and trade-offs
- Followed the existing long-name convention exactly to preserve determinism and avoid refactoring naming infrastructure.
- Inserted the new mode adjacent to its guarded mode for predictable ordering semantics in `TRACE_SUMMARY_MODE_SPECS`.

## Anything intentionally deferred
- No naming-shortening refactor was attempted; that is outside this single-task iteration.
