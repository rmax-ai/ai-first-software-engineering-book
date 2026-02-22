# Risks and decisions

## Risks discovered
- Extremely long mode-name literals increase the risk of typo-level regressions in count checks and registration entries.

## Decisions made and trade-offs
- Implemented one focused runner plus one registration tuple instead of refactoring repeated literal patterns.
- Kept all edits localized to the existing long-form guard cluster to avoid accidental adjacency/order side effects.

## Anything intentionally deferred
- Any helper-based deduplication of long mode literals remains deferred to keep this iteration strictly single-task and minimal-diff.
