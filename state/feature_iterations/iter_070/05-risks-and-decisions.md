# Risks and decisions

## Risks discovered
- Usage-example uniqueness checks only cover generated docs; they do not validate runtime behavior of parity modes.

## Decisions made and trade-offs
- Reused existing usage-example parsing helpers to keep the change minimal and deterministic.
- Scoped this iteration to one guard mode as requested, deferring broader usage-example integrity checks.

## Intentionally deferred
- Any changes to kernel/non-kernel parity execution logic.
