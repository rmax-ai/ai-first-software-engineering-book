# Risks and decisions

## Risks discovered
- `TRACE_SUMMARY_MODE_SPECS` keeps growing, so similar mode names can drift or duplicate without targeted uniqueness guards.

## Decisions made and trade-offs
- Added a focused count-based uniqueness guard instead of broader refactoring to keep this iteration minimal and deterministic.
- Preserved existing registration order to avoid unrelated behavior changes.

## Intentionally deferred
- Additional adjacency/order/uniqueness hardening for subsequent guard modes beyond the one recommended by `iter_110`.
