# Risks and Decisions

## Risks discovered
- SDK session objects may not expose `destroy()`, so teardown remains best-effort for that capability.
- Shutdown can now report session and client-stage details together, which increases message length but improves diagnosis.

## Decisions made and trade-offs
- Chose destroy-first ordering to reduce leaked session state before stopping the client process.
- Continued executing client shutdown even after session destroy failure, then surfaced the error for deterministic kernel handling.

## Anything intentionally deferred
- No additional retries/backoff were added; this remains outside current migration scope.
