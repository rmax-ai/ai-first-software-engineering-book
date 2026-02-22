# Risks and decisions

## Risks discovered
- The first registration placement inserted the new mode between the asserted neighbors, which invalidated the adjacency assertion.

## Decisions made and trade-offs
- Kept the new mode registration outside the asserted pair so the guard validates ordering without perturbing it.
- Preserved existing mode names and interfaces to avoid churn.

## Anything intentionally deferred
- Deferred additional uniqueness/order guards for the newly added adjacency mode to the next iteration.
