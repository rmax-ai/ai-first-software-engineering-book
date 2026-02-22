# Risks and decisions

## Risks discovered
- The new guard exposed two pre-existing wrapper literal mismatches; leaving them unfixed would keep this regression vector open and force guard exceptions.

## Decisions made and trade-offs
- Fixed the two mismatched wrapper literals in the same iteration to keep the new guard strict and deterministic.
- Kept validation targeted to duplicate-count smoke modes to minimize runtime while still exercising the changed surface.

## Deferred items
- None in this iteration.
