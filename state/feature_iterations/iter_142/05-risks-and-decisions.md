# Risks and Decisions

## Risks discovered
- Very long mode identifiers increase copy/paste risk for future manual edits.

## Decisions made and trade-offs
- Reused the exact existing mode strings and index-based adjacency assertions to avoid introducing helper abstractions in this minimal iteration.
- Kept scope to one runner and one mode registration to satisfy the smallest-task rule.

## Anything intentionally deferred
- No refactor of long-form mode name handling in this iteration.
