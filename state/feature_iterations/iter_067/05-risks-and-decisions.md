# Risks and decisions

## Risks discovered
- The smoke file has extensive generated coverage-guard modes; accidental ordering edits can cascade into unrelated failures.

## Decisions made and trade-offs
- Reused existing helper and failure expectations instead of introducing new helpers, keeping the diff minimal.
- Added only one new mode entry to satisfy requested symmetric coverage without broad refactors.

## Anything intentionally deferred
- No new combined kernel/non-kernel parity guard was added in this iteration.
