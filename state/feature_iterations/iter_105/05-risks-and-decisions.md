# Risks and decisions

## Risks discovered
- The new guard only protects uniqueness and adjacency for the two targeted helper hardening modes; other mode-pair uniqueness constraints remain outside this iteration.

## Decisions made and trade-offs
- Reused the existing `TRACE_SUMMARY_MODE_SPECS`-driven pattern to keep checks deterministic and avoid broad refactors.
- Kept verification scoped to the requested targeted mode to preserve one-task iteration boundaries.

## Anything intentionally deferred
- Generalized uniqueness checks for additional helper hardening guard groups were deferred to keep this iteration minimal.
