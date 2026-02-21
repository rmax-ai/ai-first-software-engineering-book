# Risks and Decisions

## Risks discovered
- Live-provider smoke remains blocked by external runtime prerequisites (credentials/service availability).

## Decisions made and trade-offs
- Did not inject fake credentials or alter provider defaults.
- Captured both credential and local-runtime availability evidence in one bounded step.

## Intentionally deferred
- Full live-provider smoke remains deferred until either `COPILOT_API_KEY` is configured or local Copilot CLI is running.
