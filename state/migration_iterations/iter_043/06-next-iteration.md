# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when both `session.destroy()` and `stop()` fail in the same shutdown path.

## Why it is next
Current coverage now includes non-callable and mixed stop-failure/destroy-unavailable branches, but it still lacks the combined dual-failure branch where both `session.destroy()` and `stop()` raise exceptions before idempotent second close.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `sdk_session.destroy` to raise `RuntimeError("forced destroy failure")` and `sdk_client.stop` to raise `RuntimeError("forced stop failure")`.
- Assert first `close()` raises `LLMClientError` containing both `session.destroy()=forced destroy failure` and `stop()=forced stop failure`.
- Assert second `close()` is a no-op and deterministic non-live modes still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
