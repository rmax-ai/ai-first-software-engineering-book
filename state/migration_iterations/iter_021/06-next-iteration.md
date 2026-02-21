# Next Iteration

## Recommended next task
Stabilize deterministic `fallback-error` smoke mode to avoid intermittent connection reset failures.

## Why it is next
The fallback HTTP error mapping regression mode is currently flaky in this environment and weakens confidence in deterministic failure-path coverage.

## Acceptance criteria
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` passes reliably across repeated local runs.
- Assertion continues to validate actionable HTTP status context.
- Command fails non-zero if mapping regresses.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
