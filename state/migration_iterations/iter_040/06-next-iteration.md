# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency when `session.destroy` is non-callable.

## Why it is next
This iteration verifies first-close success for non-callable `session.destroy`, but does not yet assert second-close no-op behavior for that exact branch.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets `session.destroy` non-callable, calls `close()` twice, and asserts no exception on either call.
- Keep existing `destroy-unavailable` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
