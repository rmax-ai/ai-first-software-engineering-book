# Risks and decisions

## Risks discovered
- Long, similarly named guard modes are easy to reorder accidentally during future edits.

## Decisions made and trade-offs
- Added one minimal order-guard mode instead of broader refactoring to keep the iteration scoped to one backlog task.
- Kept assertions index-based against `TRACE_SUMMARY_MODE_SPECS` so ordering regressions fail deterministically.

## Intentionally deferred
- Additional guard coverage for adjacency between the new `...-order-guard` mode and neighboring helper guard modes.
