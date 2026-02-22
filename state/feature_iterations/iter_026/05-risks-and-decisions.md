# Risks and Decisions

## Risks discovered
- Guard semantics could drift if future usage-mode checks bypass shared helper paths.
- Mode-spec shape changes could impact helper assumptions in multiple guards at once.

## Decisions made and trade-offs
- Added a narrow helper that accepts existing mode-spec tuples to avoid interface churn.
- Updated only the three guards requested in the previous handoff to keep scope tight.

## Intentionally deferred
- Refactoring `usage-examples-duplicates-guard` to use the same expected helper was deferred because it was not part of the acceptance criteria.
