# Next Iteration

## Recommended next task
Add deterministic smoke coverage for Copilot SDK shutdown failure handling (`stop()` and `force_stop()` paths) in `state/llm_client.py`.

## Why it is next
Bootstrap failure handling is now covered, but shutdown failure mapping remains a critical reliability path without dedicated smoke assertions.

## Acceptance criteria
- `state/copilot_sdk_smoke_test.py` includes one shutdown-failure mode.
- The mode asserts `Copilot SDK shutdown failed:` error context.
- Existing `stub`, `sdk-unavailable`, and `bootstrap-failure` modes still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
