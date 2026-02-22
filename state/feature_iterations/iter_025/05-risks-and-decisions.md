# Risks and Decisions

## Risks discovered
- Prefix-coupled parsing remains dependent on usage-line format and could break if doc line schema changes.

## Decisions made and trade-offs
- Added one minimal helper and reused it in related guard modes to reduce drift risk with low behavioral impact.
- Also reused helper in duplicates guard for consistency, while preserving duplicate detection semantics.

## Intentionally deferred
- Broader refactor of usage-doc generation/parsing contracts beyond this targeted deduplication.
