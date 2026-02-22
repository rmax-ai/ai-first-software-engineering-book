# Risks and decisions

## Risks discovered
- The guard-chain approach duplicates near-identical handlers and can increase maintenance overhead as suffix depth grows.

## Decisions made and trade-offs
- Continued with the existing table-driven deterministic pattern to keep this iteration minimal and aligned with prior iterations.
- Avoided refactoring to a generator/helper in this iteration to prevent unrelated behavioral risk.

## Intentionally deferred
- Consolidating duplicate guard handlers into a parameterized helper was deferred to keep scope limited to one smallest unfinished task.
