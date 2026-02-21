# Task

## Selected task title
Add explicit SDK session teardown in `LLMClient.close()` before client shutdown.

## Why this task now
`iter_006/06-next-iteration.md` identified session teardown as the next smallest M2 reliability hardening step to reduce leaked runtime state risk.

## Acceptance criteria for this iteration
- `state/llm_client.py::LLMClient.close()` calls `session.destroy()` when a session exists and the method is available.
- Session teardown failures map to actionable `LLMClientError` messages.
- Existing stop/force-stop fallback behavior remains intact.
