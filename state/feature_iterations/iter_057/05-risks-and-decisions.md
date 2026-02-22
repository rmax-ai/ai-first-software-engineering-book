# Risks and decisions

## Risks discovered
- The malformed-mode assertion currently targets missing `budget_signal`; other malformed payload classes (wrong payload type, missing phase event set) remain untested in this iteration.

## Decisions made and trade-offs
- **Decision:** Add a dedicated CLI mode (`trace-summary-malformed-phase`) instead of overloading the existing success mode.
- **Trade-off:** Slightly larger CLI surface, but clearer deterministic intent and simpler validation evidence.

## Intentionally deferred
- Additional malformed payload classes and table-driven malformed smoke matrix expansion were deferred to keep this iteration minimal.
