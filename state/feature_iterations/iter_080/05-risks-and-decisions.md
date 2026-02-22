# Risks and decisions

## Risks discovered
- Wrapper naming is highly repetitive, so accidental migration of extra wrappers was a key risk.

## Decisions made and trade-offs
- Limited migration to exactly two wrappers to match guidance and keep behavior changes tightly bounded.
- Preserved wrapper-specific PASS strings by passing them through helper arguments.

## Deferred
- Migrating the remaining coverage-guard wrappers to the helper.
