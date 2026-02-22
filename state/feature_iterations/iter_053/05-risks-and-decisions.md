# Risks and decisions

## Risks discovered
- Very long mode/function identifiers are brittle and can be mistyped when extending by one suffix each iteration.

## Decisions made and trade-offs
- Followed the existing explicit table-driven pattern instead of refactoring to generated entries, keeping this iteration minimal and low-risk.
- Kept validation targeted to the two commands requested by prior-iteration guidance to avoid unrelated churn.

## Intentionally deferred
- Any consolidation/refactor of repeated duplicate-count guard code blocks was deferred to keep this change scoped to one smallest unfinished task.
