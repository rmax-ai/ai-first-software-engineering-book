# Risks and Decisions

## Risks discovered
- Additional deterministic modes increase CLI mode-list length and maintenance overhead.

## Decisions made and trade-offs
- Added a separate mode instead of modifying `force-stop-unavailable` to keep existing coverage behavior stable.
- Reused existing shutdown setup/teardown helpers to keep lifecycle handling consistent.

## Intentionally deferred
- No dispatch/help-text refactor in this iteration to keep the diff minimal and focused.
