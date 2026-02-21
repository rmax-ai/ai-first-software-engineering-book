# Risks and Decisions

## Risks discovered
- Pylance reports many type diagnostics in `state/llm_client.py` due to dynamic SDK interop (`Any`, dynamic attrs, awaitability inference).
- Full live prompt-mode validation still depends on environment/auth configuration.

## Decisions made and trade-offs
- Decision: prioritize runtime-correctness and bounded shutdown semantics over extensive type refactors in this iteration.
- Decision: keep provider surface unchanged (`copilot` / `mock`) and preserve sync kernel contract.
- Trade-off: static type cleanliness remains an incremental follow-up item.

## Anything intentionally deferred
- Full typed protocol wrappers for SDK client/session interfaces.
- End-to-end non-mock planner→writer→critic iteration in this iteration artifact (requires live auth/runtime preconditions).
