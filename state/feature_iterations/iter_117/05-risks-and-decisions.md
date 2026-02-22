# Risks and decisions

## Risks discovered
- Very long mode names are fragile and easy to mis-order in `TRACE_SUMMARY_MODE_SPECS`.

## Decisions made and trade-offs
- Implemented only the smallest guard for the exact adjacency requested to avoid unrelated list refactors.
- Kept existing naming pattern to preserve consistency even though names are verbose.

## Anything intentionally deferred
- No broader cleanup of naming or ordering helpers was done; deferred to future iterations.
