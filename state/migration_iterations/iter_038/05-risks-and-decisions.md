# Risks and Decisions

## Risks discovered
- Test mode growth can make CLI help text harder to scan.

## Decisions made and trade-offs
- Added a dedicated mode instead of changing `stop-unavailable`; this keeps existing behavior stable while covering the new branch.
- Reused existing shutdown setup/teardown helpers to avoid duplicating lifecycle logic.

## Intentionally deferred
- No refactor of mode dispatch/help text structure in this iteration to keep diff minimal.
