# Risks and decisions

## Risks discovered
- The new guard checks relative ordering and presence for the two parity cleanup modes, but does not explicitly assert parser-choice uniqueness counts for that pair.

## Decisions made and trade-offs
- Reused existing parser and usage-example helper patterns to keep the diff minimal and deterministic.
- Scoped this iteration to one mode-level guard as requested, avoiding broader parser validation refactors.

## Intentionally deferred
- Adding a parity-specific parser-choice uniqueness-count guard mode.
