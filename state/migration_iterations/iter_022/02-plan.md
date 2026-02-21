# Plan

1. Reproduce fallback-error behavior and inspect `state/copilot_sdk_smoke_test.py` server handler for flake causes.
2. Apply the smallest deterministic fix in fallback error-path handlers.
3. Run targeted smoke validations including repeated `fallback-error` runs.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
