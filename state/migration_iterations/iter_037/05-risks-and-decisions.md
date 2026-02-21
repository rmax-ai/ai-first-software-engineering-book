# Risks and Decisions

## Risks discovered
- Idempotency coverage remains branch-specific; regressions in other shutdown-error combinations could still bypass this mode.

## Decisions made and trade-offs
- Added a dedicated destroy-path idempotency mode instead of widening existing modes, to keep this iteration to one minimal, explicit task.
- Kept existing `destroy-failure` mode untouched to avoid weakening prior assertions.

## Intentionally deferred
- Additional idempotency checks for `stop() unavailable` and `force_stop() unavailable` paths.
