# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` fails and `session.destroy()` is non-callable in the same run.

## Why it is next
Current coverage now handles both non-callable branches together, but does not yet cover the mixed path where shutdown first records a stop exception and then continues past a non-callable destroy branch.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `sdk_client.stop` to raise `RuntimeError("forced stop failure")` and sets `sdk_session.destroy = None`.
- Assert first `close()` raises `LLMClientError` containing `stop()=forced stop failure`, and second `close()` is a no-op.
- Keep deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`

