# Next Iteration

## Recommended next task
Add deterministic regression coverage for HTTP fallback timeout mapping in `state/copilot_sdk_smoke_test.py`.

## Why it is next
Fallback coverage now includes success, HTTP error, invalid JSON, and connection failure; timeout mapping remains unverified.

## Acceptance criteria
- New mode deterministically forces fallback timeout behavior.
- Error message includes `HTTP fallback timed out`.
- Mode exits non-zero if timeout mapping regresses.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
