# Risks and Decisions

## Risks discovered
- The shutdown smoke mode reaches private members (`client._sdk_client`) to patch async methods; this is intentional for deterministic fault injection but could require updates if internals rename.

## Decisions made and trade-offs
- Chose method patching over modifying production code so coverage increases with zero behavioral changes to `state/llm_client.py`.
- Forced both `stop()` and `force_stop()` to fail to cover the exact aggregation path in shutdown error reporting.

## Intentionally deferred
- Live provider shutdown-failure simulation was deferred because deterministic offline smoke coverage is the current migration priority.
