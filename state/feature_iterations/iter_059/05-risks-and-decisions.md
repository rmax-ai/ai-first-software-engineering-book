# Risks and Decisions

## Risks discovered
- Required-phase validation currently checks the fixed set inline; future phase additions will require coordinated updates.
- Fixture-mode validation can diverge from real kernel traces if trace generation format changes.

## Decisions made and trade-offs
- Implemented the smallest deterministic fixture change (omit only `evaluation`) to directly satisfy the requested guard.
- Kept existing mode semantics intact by adding a new explicit mode instead of overloading existing malformed-phase flags.

## Intentionally deferred
- Refactoring trace mode dispatch to a table-driven map is deferred to avoid scope expansion in this iteration.
