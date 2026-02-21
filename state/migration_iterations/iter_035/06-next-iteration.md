# Next Iteration

## Recommended next task
Add deterministic smoke coverage for repeated `close()` idempotency after shutdown failure paths.

## Why it is next
Shutdown branches are now cleaner, and validating repeated close behavior is the next smallest reliability hardening step for migration M2 shutdown robustness.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that calls `close()` twice after a forced shutdown failure scenario.
- Assert the second `close()` does not raise and does not mutate failure message expectations from the first call.
- Keep existing deterministic mode outputs unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
