# Next Iteration

## Recommended next task
Add deterministic regression coverage for HTTP fallback connection-failure mapping in `state/copilot_sdk_smoke_test.py`.

## Why it is next
Existing fallback tests now cover success, non-200, and invalid JSON; connection-failure mapping remains an uncovered failure mode from the migration test plan.

## Acceptance criteria
- New mode forces fallback transport failure without external dependencies.
- Error message includes `HTTP fallback connection failed` context.
- Mode exits non-zero if mapping regresses.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
