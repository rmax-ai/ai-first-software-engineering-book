# Risks and Decisions

## Risks discovered
- The deterministic guard chain is manually expanded and can drift if a function or mode tuple entry is missed in a future iteration.

## Decisions made and trade-offs
- Followed the existing explicit pattern for minimal diff safety instead of refactoring to a generator-based approach.
- Kept verification scoped to the exact acceptance commands to avoid unrelated churn.

## Intentionally deferred
- Refactoring repetitive duplicate-count guard handlers into data-driven generation remains deferred.
