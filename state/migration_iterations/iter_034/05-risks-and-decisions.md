# Risks and Decisions

## Risks discovered
- Deterministic smoke tests patch private internals (`_sdk_client`, `_sdk_session`), so future refactors could require fixture updates.

## Decisions and trade-offs
- Added only deterministic smoke coverage in `state/copilot_sdk_smoke_test.py` and did not modify production `state/llm_client.py` because the target branch already exists and only lacked explicit coverage.

## Intentionally deferred
- No live-provider test expansion; this iteration remains fully offline and deterministic.
