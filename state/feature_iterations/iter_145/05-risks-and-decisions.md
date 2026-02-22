# Risks and decisions

## Risks discovered
- Very long mode-name literals remain easy to mistype, which can miswire assertions to the wrong mode.

## Decisions made and trade-offs
- Reused the current explicit string-based smoke pattern instead of refactoring to shared constants to keep this one-task iteration minimal.
- Scoped validation to the new mode only to isolate impact and preserve fast feedback.

## Deferred
- Any broader deduplication/refactor of long-form mode strings remains deferred.
