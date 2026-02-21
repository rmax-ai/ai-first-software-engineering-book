# Plan

## Step-by-step plan
1. Add a new deterministic mode function for non-callable `session.destroy` in the smoke test.
2. Wire the mode into usage docs, argument choices, help text, and dispatch.
3. Run all deterministic non-live smoke modes to verify no regressions.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
