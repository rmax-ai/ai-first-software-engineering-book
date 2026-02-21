# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` is non-callable and `session.destroy` is non-callable in the same run.

## Why it is next
Current coverage validates each unavailable branch independently, but not their combined shutdown path and second-close behavior.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets both `sdk_client.stop = None` and `sdk_session.destroy = None`, then calls `close()` twice without exception.
- Keep all existing mode assertions/output unchanged.
- Keep deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
