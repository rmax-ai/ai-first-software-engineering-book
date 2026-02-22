# Risks and decisions

## Risks discovered
- The new guard enforces exact parser-choice counts for the parity mode pair, but does not yet assert contiguous placement expectations.

## Decisions made and trade-offs
- Reused existing parser/action extraction and Counter-based deterministic assertions to keep changes minimal.
- Scoped this iteration to one requested uniqueness guard mode, avoiding broader parser validation refactors.

## Intentionally deferred
- Adding a deterministic adjacency guard for parity cleanup mode ordering in argparse choices and generated usage examples.
