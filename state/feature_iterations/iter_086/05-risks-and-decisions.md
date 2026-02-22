# Risks and decisions

## Risks discovered
- The helper rollout is intentionally incremental; migrating more than two wrappers in one step would increase review and regression risk.
- PASS message strings are long and repetitive, so accidental string edits remain a risk without smoke checks.

## Decisions made and trade-offs
- Migrated exactly two wrappers (13-guard and 14-guard variants) to match prior handoff scope.
- Preserved wrapper names and PASS strings exactly, prioritizing deterministic behavior over broader cleanup.

## Deferred intentionally
- Remaining duplicate-count coverage-guard wrappers (15+ guard variants) are deferred to later iterations.
