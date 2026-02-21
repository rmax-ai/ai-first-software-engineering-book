# Task

## Selected task title
Add deterministic smoke coverage for `force_stop() unavailable` shutdown handling in `LLMClient.close()`.

## Why this task now
`iter_033/06-next-iteration.md` identified this as the next smallest unfinished reliability gap in deterministic shutdown coverage.

## Acceptance criteria for this iteration
- Add one smoke mode that patches SDK client `stop` to raise and `force_stop` to be unavailable.
- Assert `Copilot SDK shutdown failed:` appears.
- Assert `force_stop() unavailable` appears.
- Existing deterministic modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`, `stop-unavailable`, `destroy-failure`) still pass.
