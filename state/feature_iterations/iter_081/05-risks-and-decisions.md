# Risks and decisions

## Risks discovered
- The repetitive wrapper names make it easy to migrate more than the intended two wrappers by mistake.

## Decisions made and trade-offs
- Migrated only the two wrappers explicitly requested by iter_080 guidance.
- Kept PASS output strings unchanged to avoid perturbing deterministic smoke output.

## Deferred
- Migration of the remaining duplicate-count coverage-guard wrappers to the helper.
