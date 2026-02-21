# Risks and Decisions

## Risks discovered
- `--mode live` remains environment-dependent and was not exercised in this iteration.

## Decisions made and trade-offs
- Kept validation focused on deterministic local modes (`stub`, `sdk-unavailable`) to ensure reproducible evidence.
- Removed only fallback-specific smoke code, leaving supported mode behavior unchanged.

## Intentionally deferred
- Live-provider validation and any further SDK ergonomics changes.
