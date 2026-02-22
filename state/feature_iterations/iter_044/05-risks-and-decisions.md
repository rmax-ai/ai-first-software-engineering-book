# Risks and decisions

## Risks discovered
- Very long mode strings increase risk of mismatches across handler names, mode literals, and registration entries.

## Decisions made and trade-offs
- Followed the existing explicit chain pattern to keep this iteration minimal and predictable.

## Intentionally deferred
- Any refactor to generate duplicate-count coverage guards programmatically was deferred to preserve one-task scope.
