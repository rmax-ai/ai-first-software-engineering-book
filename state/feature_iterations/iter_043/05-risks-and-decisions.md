# Risks and decisions

## Risks discovered
- Mode-name strings are intentionally long; manual edits can introduce mismatch risk between handler name, target mode string, and mode-spec registration.

## Decisions made and trade-offs
- Followed the existing explicit chain pattern instead of refactoring to generated tests to keep this iteration minimal and aligned with backlog guidance.

## Intentionally deferred
- Any consolidation/refactor of repetitive duplicate-count guard handlers was deferred to preserve one-task scope.
