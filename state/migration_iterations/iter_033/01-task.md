# Task

## Selected task title
Add deterministic `stop-unavailable` smoke coverage for `LLMClient.close()` shutdown aggregation.

## Why this task now
`iter_032/06-next-iteration.md` identified the uncovered shutdown branch where SDK client `stop` is not callable.

## Acceptance criteria
- Add `--mode stop-unavailable` to `state/copilot_sdk_smoke_test.py`.
- Assert shutdown message includes `Copilot SDK shutdown failed:`.
- Assert shutdown message includes `stop() unavailable`.
- Existing deterministic modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`, `destroy-failure`) still pass.
