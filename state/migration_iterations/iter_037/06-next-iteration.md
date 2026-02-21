# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` is unavailable.

## Why it is next
Destroy-path idempotency is now covered; `stop() unavailable` is the next smallest shutdown branch without repeated-close regression protection.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `stop` to non-callable, calls `close()` twice, and asserts only the first call raises.
- Keep existing `stop-unavailable` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
