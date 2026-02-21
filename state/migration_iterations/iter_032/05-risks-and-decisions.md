# Risks and Decisions

## Risks discovered
- Smoke coverage relies on internal attributes (`_sdk_session`, `_sdk_client`), so internal refactors could require test updates.

## Decisions and trade-offs
- Kept scope to smoke-test-only changes for minimal migration risk.
- Reused the existing shutdown-failure pattern to keep deterministic behavior and consistency.

## Deferred intentionally
- No live-provider changes or additional runtime shutdown logic changes were made.
