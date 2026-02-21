# Next Iteration

## Recommended next task
Add deterministic smoke coverage for `force_stop() unavailable` shutdown handling in `LLMClient.close()`.

## Why it is next
Current deterministic modes now cover stop exceptions and stop unavailability, but not the branch where `stop()` fails and `force_stop` is not callable.

## Acceptance criteria
- Add one smoke mode that patches SDK client `stop` to raise and `force_stop` to be unavailable.
- Assert `Copilot SDK shutdown failed:` appears.
- Assert `force_stop() unavailable` appears.
- Existing deterministic modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`, `stop-unavailable`, `destroy-failure`) still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
