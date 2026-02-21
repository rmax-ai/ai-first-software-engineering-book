# Risks and Decisions

## Risks discovered
- Validation is behavioral and unit-scoped; live-provider field variance in production remains dependent on provider behavior.

## Decisions made and trade-offs
- Kept scope to normalized extraction logic guarantees without introducing new test harness files.
- Avoided unrelated refactors; this iteration is evidence-only.

## Intentionally deferred
- Live provider smoke remains deferred due external credential/runtime prerequisites.
