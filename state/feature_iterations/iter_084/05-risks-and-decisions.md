# Risks and decisions

## Risks discovered
- The helper-rollout sequence depends on continuing strict one-step migrations; touching too many wrappers in one iteration increases review risk.
- PASS message strings are long and repetitive, so accidental edits are easy without targeted smoke checks.

## Decisions made and trade-offs
- Migrated exactly two wrappers (9-guard and 10-guard variants) to match prior handoff scope.
- Preserved wrapper names and PASS strings exactly, trading speed for safer incrementalism.

## Deferred intentionally
- Remaining duplicate-count coverage-guard wrappers (11+ guard variants) remain for later iterations.

