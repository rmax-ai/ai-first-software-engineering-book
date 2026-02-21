# Task

## Selected task title
Harden Copilot SDK shutdown in `LLMClient.close()` with stop-first and force-stop fallback.

## Why this task now
`iter_005/06-next-iteration.md` identified robust shutdown fallback as the next smallest M2 reliability step.

## Acceptance criteria
- `close()` calls `stop()` first and uses `force_stop()` only when stop fails.
- Shutdown failures surface actionable `LLMClientError` messages.
- No behavior change when SDK client was never initialized.
