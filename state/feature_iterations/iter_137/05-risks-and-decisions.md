# Risks and decisions

## Risks discovered
- Extremely long mode names are error-prone when adding new wrappers and registration entries.

## Decisions made and trade-offs
- Followed the existing wrapper/helper naming and registration order pattern instead of introducing new abstractions, to keep this diff minimal and deterministic.
- Added only one new mode and one new function to satisfy the requested smallest unfinished task.

## Anything intentionally deferred
- Additional refactoring of long mode-name constants was deferred because it is unrelated to this single-task iteration.
