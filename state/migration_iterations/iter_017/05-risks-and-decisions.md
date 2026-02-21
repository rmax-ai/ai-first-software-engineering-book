# Risks and Decisions

## Risks discovered
- The smoke test is script-style, so fallback behavior is covered indirectly rather than through a formal unit test framework.

## Decisions and trade-offs
- Kept scope to one file and one focused scenario to satisfy the single-task iteration rule.
- Reused the existing smoke test assertions to avoid broad test harness changes.

## Intentionally deferred
- Additional failure-path scenarios (e.g., `session.error` mapping) are deferred to the next iteration.
