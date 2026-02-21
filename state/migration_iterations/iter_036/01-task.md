# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency after shutdown failure.

## Why this task now
`iter_035/06-next-iteration.md` prioritized validating repeated close behavior to harden M2 shutdown reliability paths.

## Acceptance criteria for this iteration
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that calls `close()` twice after a forced shutdown failure scenario.
- Assert the second `close()` does not raise and does not mutate failure message expectations from the first call.
- Keep existing deterministic mode outputs unchanged.
