# Next Iteration

## Recommended next task
Add a deterministic smoke mode to validate `session.destroy()` failure handling in `LLMClient.close()`.

## Why it is next
`close()` aggregates `session.destroy()` failures with shutdown errors, but current smoke coverage only exercises `stop()/force_stop()` failures.

## Acceptance criteria
- `state/copilot_sdk_smoke_test.py` includes one `destroy-failure` mode.
- The mode asserts `Copilot SDK shutdown failed:` and `session.destroy()=` error context.
- Existing `stub`, `sdk-unavailable`, `bootstrap-failure`, and `shutdown-failure` modes still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
