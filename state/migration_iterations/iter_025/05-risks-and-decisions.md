# Risks and Decisions

## Risks discovered
- The coverage targets only smoke behavior and does not run as part of a broader automated test suite by default.

## Decisions and trade-offs
- Chose a local deterministic HTTP server returning `["not-an-object"]` to directly exercise the exact `state/llm_client.py` non-object mapping branch.
- Kept the scope strictly to one task from prior handoff guidance.

## Intentionally deferred
- Any refactor/removal of HTTP fallback behavior itself is deferred to a later migration task.

