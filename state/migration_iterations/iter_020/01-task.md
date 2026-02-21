# Task

## Selected task title
Add deterministic fallback HTTP error mapping regression mode to `state/copilot_sdk_smoke_test.py`.

## Why this task now
`iter_019/06-next-iteration.md` prioritized protecting fallback failure-path error mapping as the next highest-risk gap.

## Acceptance criteria
- Smoke test can force fallback path and return HTTP 500 payload.
- Mode asserts `LLMClientError` contains HTTP status context.
- Command exits non-zero if fallback error mapping regresses.
