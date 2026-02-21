# Task

## Selected task title
Add deterministic `destroy-failure` smoke coverage for `LLMClient.close()` shutdown aggregation.

## Why this task now
`iter_031/06-next-iteration.md` identified missing deterministic coverage for `session.destroy()` failures.

## Acceptance criteria
- Add `--mode destroy-failure` to `state/copilot_sdk_smoke_test.py`.
- Assert shutdown message includes `Copilot SDK shutdown failed:`.
- Assert shutdown message includes `session.destroy()=` detail.
- Existing smoke modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`) still pass.
