# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `force_stop()` is unavailable.

## Why it is next
M2 shutdown idempotency is now covered for generic shutdown failure, destroy failure, and stop-unavailable; force-stop-unavailable idempotency is the next smallest uncovered shutdown branch.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `stop()` to fail and `force_stop` to non-callable, calls `close()` twice, and asserts only the first call raises.
- Keep existing `force-stop-unavailable` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
