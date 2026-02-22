# Risks and Decisions

## Risks discovered
- Suffix checks rely on the current `" mode validates "` delimiter; future message format refactors must update this guard.

## Decisions made and trade-offs
- Reused AST parsing approach from adjacent guards to keep deterministic behavior and minimize implementation churn.
- Enforced semantic suffix shape (`duplicate-count ... mode coverage`) instead of hard-coding per-wrapper full literals for lower maintenance.

## Anything intentionally deferred
- Full literal strictness for every wrapper PASS message remains covered by existing literal guard modes and is not expanded here.
