# Risks and Decisions

## Risks discovered
- Initial registration of the new mode between the uniqueness guard and `usage-examples-order-guard` broke the intended adjacency invariant.

## Decisions made and trade-offs
- Registered the new mode immediately before the uniqueness guard so the new check can execute while preserving the required adjacency relation it validates.
- Kept scope to one guard and one targeted verification command to satisfy the single-task iteration rule.

## Intentionally deferred
- Broader ordering audits across all duplicate-count wrapper guard modes were deferred to a follow-up iteration.
