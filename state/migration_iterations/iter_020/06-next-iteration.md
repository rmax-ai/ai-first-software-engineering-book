# Next Iteration

## Recommended next task
Add deterministic regression coverage for HTTP fallback invalid JSON handling.

## Why it is next
Fallback error status mapping is now covered; invalid JSON parsing remains an uncovered high-risk failure branch.

## Acceptance criteria
- Add a smoke mode that forces fallback path and returns non-JSON payload.
- Assert `LLMClientError` includes `HTTP fallback returned invalid JSON` context.
- Mode fails non-zero on regression.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
