# Risks and decisions

## Risks discovered
- Extremely long mode names remain prone to typographical drift when adding new guards.

## Decisions made and trade-offs
- Reused the existing adjacency-assertion guard pattern to minimize risk and keep the diff small.
- Limited scope to one requested guard mode and avoided helper refactors in this iteration.

## Anything intentionally deferred
- Any broader simplification of long mode-name literals or helper abstraction remains deferred.
