# Risks and decisions

## Risks discovered
- AST-based guard inspects wrapper source; major refactors to wrapper generation style may require guard adjustment.

## Decisions and trade-offs
- Chose a minimal call-shape check (arg count + no keywords) to match requested scope and avoid duplicating existing literal checks.

## Intentionally deferred
- Additional argument-type checks beyond positional-only semantics.
