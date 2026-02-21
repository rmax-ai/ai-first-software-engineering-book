# Risks and Decisions

## Risks discovered
- Some SDK implementations may expose non-async or missing shutdown hooks; current handling reports this clearly but does not recover beyond available hooks.

## Decisions made and trade-offs
- Treated missing `stop()` as shutdown failure and attempted `force_stop()` as fallback to keep teardown bounded.
- Kept shutdown logic in `close()` only, avoiding interface changes in kernel or chat call paths.

## Intentionally deferred
- Explicit session-destroy teardown before client stop was deferred to keep this iteration single-scope.
