# Risks and Decisions

## Risks discovered
- The new guard intentionally focuses on f-strings and concatenation nodes; other non-literal expression forms remain covered by existing signature/literal guards.

## Decisions made and trade-offs
- Reused existing AST inspection pattern for consistency with prior duplicate-count guard modes.
- Limited scope to one new guard mode to keep diff minimal and deterministic.

## Intentionally deferred
- Broader helper-call normalization checks beyond literal-only enforcement.
