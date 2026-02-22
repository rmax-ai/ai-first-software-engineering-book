# Risks and decisions

## Risks discovered
- Similar long-form mode names can drift in ordering unless each new invariant gets explicit guard coverage.

## Decisions made and trade-offs
- Added a focused adjacency guard mode instead of broader refactoring to keep this iteration minimal.
- Reordered a small section of `TRACE_SUMMARY_MODE_SPECS` so the guarded adjacency reflects the intended invariant.

## Intentionally deferred
- Additional hardening for adjacency relationships involving `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard`.
