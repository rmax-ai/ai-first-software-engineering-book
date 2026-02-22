# Risks and decisions

## Risks discovered
- Very long mode names increase the chance of accidental string mismatches during wrapper migration.

## Decisions made and trade-offs
- Migrated only the two wrappers requested by the prior iteration guidance.
- Kept PASS strings byte-for-byte unchanged to preserve deterministic smoke output.

## Deferred
- Migration of remaining duplicate-count coverage-guard wrappers.
