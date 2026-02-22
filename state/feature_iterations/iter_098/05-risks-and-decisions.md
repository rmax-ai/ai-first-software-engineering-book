# Risks and decisions

## Risks discovered
- The guard validates static string literals in wrapper source; it does not execute wrapper functions with dynamic formatting.

## Decisions made and trade-offs
- Reused existing AST-inspection patterns from adjacent duplicate-count wrapper guards to keep behavior deterministic and diffs minimal.
- Kept validation scoped to targeted smoke modes to match the smallest-task iteration contract.

## Deferred work
- Potential future guard for stricter PASS message suffix canonicalization beyond prefix structure.
