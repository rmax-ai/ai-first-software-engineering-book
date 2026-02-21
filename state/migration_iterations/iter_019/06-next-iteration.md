# Next Iteration

## Recommended next task
Add one deterministic regression mode in `state/copilot_sdk_smoke_test.py` for fallback HTTP error mapping (non-200 response).

## Why this is next
Fallback success behavior is now covered; the next highest-risk gap is verifying actionable error mapping for fallback failures.

## Acceptance criteria
- Smoke test can force fallback path and return HTTP 500 payload.
- Mode asserts `LLMClientError` message includes HTTP status context.
- Command exits non-zero if fallback error mapping regresses.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
