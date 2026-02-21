# Next Iteration

## Recommended next task
Add a deterministic smoke-test mode that simulates SDK worker-loop bootstrap timeout/failure and asserts the new `LLMClientError` messages.

## Why it is next
Current smoke checks validate happy-path and SDK-unavailable behavior, but do not directly lock in bootstrap failure handling.

## Acceptance criteria
- `state/copilot_sdk_smoke_test.py` includes one mode for bootstrap timeout/failure simulation.
- The mode asserts `Copilot SDK worker-loop bootstrap` error context.
- Existing `stub` and `sdk-unavailable` modes still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
