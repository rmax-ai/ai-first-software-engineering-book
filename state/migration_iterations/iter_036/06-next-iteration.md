# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency after `session.destroy()` failure.

## Why it is next
Current idempotency coverage exercises stop/force_stop failures only; a destroy-specific path is the next smallest branch to harden shutdown reliability.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that forces `session.destroy()` failure, calls `close()` twice, and asserts only the first call raises.
- Preserve existing `destroy-failure` assertions and output text.
- Keep all existing deterministic modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
