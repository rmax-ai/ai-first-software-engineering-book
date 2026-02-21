# Task

## Selected task title
Reintroduce legacy HTTP fallback for `state/llm_client.py` when Copilot SDK is unavailable.

## Why this task now
`state/copilot-sdk-migration-plan.md` M0 requires keeping the existing HTTP implementation as a fallback path while introducing the SDK-backed path.

## Acceptance criteria
- `LLMClient(provider="copilot")` still uses SDK path when available.
- If SDK import is unavailable, client falls back to HTTP chat completions using `--llm-base-url`.
- Response content and token usage are normalized into `LLMResponse`/`LLMUsage`.
