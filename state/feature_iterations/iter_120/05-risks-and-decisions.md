# Risks and decisions

## Risks discovered
- Long literal mode names remain easy to mistype when extending guard coverage.

## Decisions made and trade-offs
- Reused the existing uniqueness-guard shape to keep the diff minimal and deterministic.
- Kept the iteration scoped to one guard mode and one registration entry.

## Anything intentionally deferred
- Any broader refactor for long mode-name literals remains deferred.
