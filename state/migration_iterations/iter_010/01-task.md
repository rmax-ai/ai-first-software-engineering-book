# Task

## Selected task title
Validate `LLMClient` failure-path behavior for SDK/legacy boundary without kernel chapter eligibility dependency.

## Why this task now
`iter_009` showed kernel-level regression is blocked by governance status. Migration test plan still requires failure-path validation.

## Acceptance criteria for this iteration
- Missing API key on `openai_compatible` raises actionable `LLMClientError`.
- Transport failure on `ollama` path raises actionable `LLMClientError`.
- `mock` provider deterministic behavior remains unchanged.
