# Risks and Decisions

## Risks discovered
- Delimiter-count checks depend on the current canonical delimiter token (` mode validates `); if message format changes intentionally, this guard must be updated with the new canonical token.

## Decisions made and trade-offs
- Reused existing AST-based wrapper-source inspection patterns to keep behavior deterministic and avoid broad refactors.
- Enforced delimiter multiplicity only (exactly one) rather than full message reconstruction to keep the guard small and focused while complementing existing literal/prefix/suffix guards.

## Anything intentionally deferred
- Full per-wrapper literal normalization remains delegated to existing literal/prefix/suffix guard modes.
