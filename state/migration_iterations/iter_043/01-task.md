# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` fails and `session.destroy()` is non-callable in the same run.

## Why this task now
`iter_042/06-next-iteration.md` marked this mixed shutdown path as the next smallest missing hardening case.

## Acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `sdk_client.stop` to raise `RuntimeError("forced stop failure")` and sets `sdk_session.destroy = None`.
- First `close()` raises `LLMClientError` containing `stop()=forced stop failure`, and second `close()` is a no-op.
- Keep deterministic non-live modes passing.
