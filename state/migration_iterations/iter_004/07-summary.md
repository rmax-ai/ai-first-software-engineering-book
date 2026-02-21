# Summary

This iteration completed one focused migration hardening task: SDK usage extraction normalization in `state/llm_client.py`.
The response normalizer now routes usage parsing through dedicated helpers instead of only direct dict fields.
The client now supports both direct usage payloads and aggregated `assistant.usage` event lists.
Token key normalization accepts `prompt/completion` and `input/output` variants while preserving `LLMUsage` schema.
No public interface changes were made to `LLMClient.chat(...)`.
Mock and legacy HTTP provider paths were left untouched.
Targeted validation passed via py_compile and a direct smoke assertion script (`validation-ok`).
Next iteration should focus on clearer SDK failure mapping to `LLMClientError` paths.
