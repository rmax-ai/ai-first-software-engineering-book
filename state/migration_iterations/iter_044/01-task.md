# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when both `stop()` and `session.destroy()` fail in the same shutdown path.

## Why this task now
`iter_043/06-next-iteration.md` identified the dual-failure shutdown branch as the next smallest missing hardening case.

## Acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `sdk_client.stop` and `sdk_session.destroy` to raise forced runtime failures.
- First `close()` raises `LLMClientError` containing both `stop()=forced stop failure` and `session.destroy()=forced destroy failure`.
- Second `close()` is a no-op and deterministic non-live smoke modes still pass.
