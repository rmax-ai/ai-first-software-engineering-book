# Next Iteration

## Recommended next task
Add deterministic regression coverage for HTTP fallback non-object payload mapping in `state/copilot_sdk_smoke_test.py`.

## Why it is next
Fallback coverage now includes success, HTTP error, invalid JSON, connection failure, and timeout; non-object JSON response handling remains unverified.

## Acceptance criteria
- New mode deterministically returns a JSON payload that is not an object (for example, a list).
- Error message includes `HTTP fallback returned non-object payload`.
- Mode exits non-zero if the mapping regresses.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
