# Risks and Decisions

## Risks discovered
- Extremely long mode identifiers remain fragile and easy to mistype.

## Decisions made and trade-offs
- Followed existing naming and wrapper style exactly to minimize diff size and keep ordering semantics consistent with prior iterations.
- Scoped validation to the newly added mode to keep runtime short while still proving the changed surface.

## Intentionally deferred
- No refactor of long mode-name construction was attempted to avoid unrelated churn.
