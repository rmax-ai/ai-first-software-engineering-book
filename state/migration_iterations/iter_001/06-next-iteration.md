# Next Iteration

## Recommended next task
Add a focused regression in `state/copilot_sdk_smoke_test.py` that permanently covers the HTTP fallback path.

## Why this is next
The fallback behavior is now implemented and should be protected by a committed, repeatable test path instead of an ad-hoc inline harness.

## Acceptance criteria
- Smoke test suite includes a deterministic fallback-mode case.
- Test verifies content extraction and usage extraction from HTTP fallback response.
- Test exits non-zero on fallback regressions.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
