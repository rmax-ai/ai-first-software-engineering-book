# Risks and decisions

## Risks discovered
- Mode names are extremely long and differ by small suffixes, so string-level mistakes can silently point guards at the wrong mode.

## Decisions made and trade-offs
- Kept scope to one new guard function and one new mode registration to satisfy the exact backlog step with minimal diff.
- Used the same assertion/print style as existing guard modes to preserve consistency and avoid broad refactors.

## Anything intentionally deferred
- No refactoring of long mode-name constants into shared aliases; deferred to keep this iteration minimal.
