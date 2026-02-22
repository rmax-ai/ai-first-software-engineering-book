# Risks and decisions

## Risks discovered
- The new guard partially overlaps existing mode-name and PASS-prefix guards, so future edits should keep assertions complementary and not contradictory.

## Decisions made and trade-offs
- Implemented the smallest requested guard slice from prior iteration guidance without refactoring neighboring guards.
- Reused established AST call-parsing pattern to keep behavior deterministic and consistent with surrounding tests.

## Anything intentionally deferred
- Deduplicating overlapping wrapper guard logic into shared helpers was deferred to avoid unrelated refactor scope.
