# Summary

This iteration completed one migration task: enforcing SDK-only behavior for Copilot provider calls.
`state/llm_client.py` now returns SDK chat results directly and no longer falls back to HTTP routing.
When SDK import fails or the SDK module is incomplete, `LLMClientError` is raised with clear guidance.
`state/copilot_sdk_smoke_test.py` now uses `sdk-unavailable` mode to validate this behavior.
Targeted validation ran in `stub` and `sdk-unavailable` modes.
Both validation commands passed with exit code 0.
Scope stayed minimal and limited to the requested migration step.
