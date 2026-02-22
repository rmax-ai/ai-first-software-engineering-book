# Risks and decisions

## Risks discovered
- Guard-mode names are now very long; typo risk increases with each incremental suffix.
- Registration-order assertions can become brittle if future edits reorder unrelated modes.

## Decisions made and trade-offs
- Followed the existing explicit-string pattern instead of introducing abstractions, minimizing scope and preserving local consistency.
- Added exactly one function and one mode registration to satisfy the single-task iteration contract.

## Intentionally deferred
- No refactor of mode-name construction/helpers.
- No broader smoke matrix changes beyond this one uniqueness-count guard.

