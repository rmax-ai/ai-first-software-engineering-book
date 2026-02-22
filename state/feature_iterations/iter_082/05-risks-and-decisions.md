# Risks and decisions

## Risks discovered
- Long repetitive wrapper names increase the chance of touching the wrong function while doing incremental migrations.

## Decisions made and trade-offs
- Migrated only the two wrappers requested by iter_081 guidance.
- Kept PASS output strings unchanged to preserve deterministic smoke output text.

## Deferred
- Migration of the remaining duplicate-count coverage-guard wrappers to the helper.
