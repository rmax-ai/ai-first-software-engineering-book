# Risks and decisions

## Risks discovered
- Additional parity guard modes added later could bypass the helper if contributors duplicate literals instead of reusing the helper.

## Decisions made and trade-offs
- Added one small helper and migrated existing parity guard callsites only, avoiding broader refactors to keep this iteration focused.
- Preserved existing assertion messages and behavior to minimize regression risk.

## Intentionally deferred
- Consolidating repeated parser `--mode` action lookup code across guard functions was deferred because it is outside this iteration's single accepted task.
