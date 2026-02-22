# Risks and Decisions

## Risks discovered
- The smoke mode registry is long and append-only; ordering assertions can become brittle if unrelated insertion points are changed.

## Decisions made and trade-offs
- Added a focused adjacency-order assertion instead of broader registry refactoring to keep this iteration minimal and deterministic.
- Kept naming consistent with prior guard modes even though it is verbose, because mode names act as stable test interfaces.

## Intentionally deferred
- Additional uniqueness-count checks for the new mode were deferred to a future iteration to keep scope to one smallest unfinished task.
