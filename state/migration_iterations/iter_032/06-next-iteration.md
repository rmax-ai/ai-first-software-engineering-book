# Next Iteration

## Recommended next task
Add deterministic smoke coverage for `stop() unavailable` shutdown handling in `LLMClient.close()`.

## Why it is next
Current deterministic smoke modes validate `destroy()` failure and `stop()/force_stop()` exceptions, but not the branch where SDK client lacks `stop()`.

## Acceptance criteria
- Add one smoke mode that patches SDK client to remove or disable callable `stop`.
- Assert `Copilot SDK shutdown failed:` appears.
- Assert `stop() unavailable` appears.
- Existing deterministic modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`, `destroy-failure`) still pass.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
