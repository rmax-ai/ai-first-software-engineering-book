# Risks and Decisions

## Risks discovered
- Cleanup exceptions from provider-specific client implementations will propagate and can still fail the run during teardown.

## Decisions and trade-offs
- Chose explicit `close()` then `stop()` fallback to preserve compatibility with both current and upcoming SDK-backed clients.
- Kept change localized to `run_kernel(...)` rather than broader refactoring to minimize migration risk.

## Intentionally deferred
- SDK-backed transport path in `state/llm_client.py` is still pending.
