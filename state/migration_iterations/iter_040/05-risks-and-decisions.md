# Risks and Decisions

## Risks discovered
- The shutdown branch for non-callable `session.destroy` intentionally does not raise, so regressions could silently change behavior without deterministic coverage.

## Decisions made and trade-offs
- Added a dedicated deterministic mode rather than broad refactoring to keep the change minimal and targeted.
- Kept existing `destroy-failure` behavior and output untouched to avoid destabilizing prior coverage.

## Intentionally deferred
- Additional lifecycle edge-case coverage beyond this single branch remains deferred to the next iteration.
