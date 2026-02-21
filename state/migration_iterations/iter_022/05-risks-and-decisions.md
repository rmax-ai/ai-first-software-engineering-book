# Risks and Decisions

## Risks discovered
- Local HTTP handler tests can flake when request bodies are not fully consumed before writing responses.

## Decisions made and trade-offs
- Chose a minimal deterministic fix (read and discard request body) instead of broader test harness refactors.
- Kept assertion semantics unchanged to preserve existing failure signaling.

## Intentionally deferred
- No new transport/retry logic was added to `state/llm_client.py`; this iteration focused strictly on smoke-test determinism.
