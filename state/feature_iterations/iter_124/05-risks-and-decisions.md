# Risks and decisions

## Risks discovered
- Mode names are very long and easy to mistype, creating fragile string-based regressions.

## Decisions made and trade-offs
- Followed existing explicit-string guard pattern instead of introducing abstractions, preserving deterministic behavior and minimizing diff size.
- Kept validation scoped to the newly added mode for fast, targeted signal.

## Anything intentionally deferred
- Broader refactoring of long mode-name constants was deferred to avoid unrelated churn.
