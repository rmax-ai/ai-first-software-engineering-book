# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` is unavailable and `session.destroy()` fails in the same shutdown path.

## Why it is next
Current coverage now includes both-unavailable, stop-failure+destroy-unavailable, and both-failure branches, but it still lacks the mixed branch where `stop()` is non-callable while `session.destroy()` raises.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets `sdk_client.stop = None` and patches `sdk_session.destroy` to raise `RuntimeError("forced destroy failure")`.
- Assert first `close()` raises `LLMClientError` containing both `stop() unavailable` and `session.destroy()=forced destroy failure`.
- Assert second `close()` is a no-op and deterministic non-live modes still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
