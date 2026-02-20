# Summary

This iteration implemented the recommended SDK adapter step in `state/llm_client.py`.
`LLMClient.chat(...)` now keeps mock behavior unchanged, tries a guarded Copilot SDK path for non-mock providers, and falls back to legacy HTTP methods when SDK is unavailable/disabled.
The client now tracks lazy SDK client/session handles and normalizes SDK output into existing `LLMResponse`/`LLMUsage` structures.
`close()` was extended to stop/force-stop SDK client instances when present.
Targeted validation succeeded with `python -m py_compile state/llm_client.py state/kernel.py`.
The next iteration should harden usage aggregation from SDK event-stream data.
