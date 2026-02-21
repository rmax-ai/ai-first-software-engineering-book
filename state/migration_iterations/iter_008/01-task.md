# Task

## Selected task title
Reset SDK client/session references after successful shutdown in `LLMClient.close()`.

## Why this task now
`iter_007` identified stale SDK handle reuse risk across repeated runs. Clearing handles after successful shutdown is the smallest remaining reliability hardening step.

## Acceptance criteria for this iteration
- `close()` sets `_sdk_client` and `_sdk_session` to `None` after successful shutdown paths.
- Error paths keep actionable `LLMClientError` details.
- Existing provider behavior remains unchanged.
