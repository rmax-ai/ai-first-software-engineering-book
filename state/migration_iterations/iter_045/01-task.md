# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` is unavailable and `session.destroy()` fails.

## Why this task now
`iter_044/06-next-iteration.md` identified this mixed shutdown branch as the next smallest uncovered hardening case.

## Acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets `sdk_client.stop = None` and patches `sdk_session.destroy` to raise `RuntimeError("forced destroy failure")`.
- Assert first `close()` raises `LLMClientError` containing both `stop() unavailable` and `session.destroy()=forced destroy failure`.
- Assert second `close()` is a no-op and deterministic non-live smoke modes still pass.
