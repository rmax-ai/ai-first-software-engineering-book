# Risks and Decisions

## Risks discovered
- Mode names are intentionally long; a typo in either function names or mode strings can silently break discoverability.

## Decisions made and trade-offs
- Followed the existing wrapper-guard naming pattern instead of introducing helper abstraction to keep this iteration minimal and low risk.
- Registered the new mode immediately after the newest adjacency-order guard entry to maintain local readability of related guards.

## Anything intentionally deferred
- No refactor of long string constants into shared constants; deferred to avoid unrelated churn.
