# Risks and decisions

## Risks discovered
- Long literal mode names remain easy to mistype when extending guard coverage.

## Decisions made and trade-offs
- Reused the existing adjacency-guard pattern to keep the diff minimal and deterministic.
- Kept scope to one guard mode plus one registration entry.

## Anything intentionally deferred
- Any broader refactor to centralize long mode-name literals remains deferred.
