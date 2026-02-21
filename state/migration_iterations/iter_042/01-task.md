# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when both `stop()` and `session.destroy()` are non-callable.

## Why this task now
`iter_041/06-next-iteration.md` identified the combined non-callable shutdown path as the next smallest missing hardening case.

## Acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets `sdk_client.stop = None` and `sdk_session.destroy = None`.
- First `close()` call raises `LLMClientError` with shutdown context; second `close()` call is a no-op.
- Keep existing deterministic non-live modes passing.
