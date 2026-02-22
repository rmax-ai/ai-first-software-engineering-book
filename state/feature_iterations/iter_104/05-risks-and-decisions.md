# Risks and decisions

## Risks discovered
- The new guard checks ordering inside `TRACE_SUMMARY_MODE_SPECS`; it does not directly re-check wrapper helper AST semantics, which remain covered by existing modes.

## Decisions made and trade-offs
- Reused existing guard-mode style and assertions to keep this change minimal and deterministic.
- Scoped verification to the requested targeted smoke mode to satisfy one-task iteration boundaries.

## Anything intentionally deferred
- Additional uniqueness checks for these two helper hardening modes were deferred to a later iteration to keep this change focused on adjacency ordering.
