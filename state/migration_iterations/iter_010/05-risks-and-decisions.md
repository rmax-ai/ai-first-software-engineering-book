# Risks and Decisions

## Risks discovered
- Kernel-level integration validation is still blocked by chapter eligibility governance state.

## Decisions made and trade-offs
- Focused this iteration on directly testable `LLMClient` failure paths rather than changing governance state.
- Kept scope to evidence gathering; no source code changes were necessary.

## Intentionally deferred
- End-to-end kernel-level mock run with trace/resource accounting remains deferred until at least one chapter is eligible.
