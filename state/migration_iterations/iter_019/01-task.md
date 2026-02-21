# Task

## Selected task title
Add a deterministic HTTP fallback regression mode to `state/copilot_sdk_smoke_test.py`.

## Why this task now
Prior iteration guidance explicitly requested a committed fallback regression so HTTP fallback behavior stays protected.

## Acceptance criteria
- Smoke test suite includes a deterministic fallback mode.
- Fallback mode verifies response content and usage extraction from fallback HTTP response.
- Fallback mode fails the process on regressions.
