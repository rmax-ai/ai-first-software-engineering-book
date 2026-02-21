# Risks and Decisions

## Risks discovered
- Existing `fallback-error` mode appears flaky in this environment due occasional connection reset during HTTP error body reads.

## Decisions made and trade-offs
- Kept scope to the requested invalid JSON branch and avoided broad refactors in fallback transport handling.
- Reused existing forced-fallback test pattern for minimal behavioral drift.

## Intentionally deferred
- Stabilizing `fallback-error` mode transport timing/teardown behavior.
