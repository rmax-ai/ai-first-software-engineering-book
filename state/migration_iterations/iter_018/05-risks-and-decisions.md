# Risks and Decisions

## Risks discovered
- HTTP fallback assumes OpenAI-compatible `POST /v1/chat/completions` response shape.

## Decisions made and trade-offs
- Used stdlib `urllib` for minimal dependency footprint and compatibility with existing module constraints.
- Triggered fallback only when SDK is unavailable, not on runtime SDK errors, to avoid masking SDK failures.

## Intentionally deferred
- Broader schema compatibility for non-OpenAI chat completion responses.
