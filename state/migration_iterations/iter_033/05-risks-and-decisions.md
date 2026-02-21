# Risks and Decisions

## Risks discovered
- Smoke coverage patches internal attributes (`_sdk_client`, `_sdk_session`), so internal shutdown refactors could require smoke updates.

## Decisions and trade-offs
- Kept scope to deterministic smoke-test-only changes for minimal migration risk.
- Reused the established shutdown-failure test structure to keep behavior and assertions consistent.

## Deferred intentionally
- No runtime shutdown logic changes in `state/llm_client.py` were made.
