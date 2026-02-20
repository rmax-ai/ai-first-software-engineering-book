# Risks and Decisions

## Risks discovered
- Runtime compatibility depends on the installed Copilot SDK Python package exposing expected symbols (`CopilotClient`, `CopilotClientOptions`, `SessionConfig`).

## Decisions made and trade-offs
- Used guarded import (`importlib.import_module("copilot")`) and only fallback when SDK is absent/disabled.
- Chose minimal response normalization to preserve current `LLMResponse` shape without broad kernel changes.

## Intentionally deferred
- Full event-stream (`assistant.usage`) aggregation for providers with non-dict SDK responses.
