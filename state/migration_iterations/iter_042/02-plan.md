# Plan

1. Add a focused combined unavailable/idempotency mode to `state/copilot_sdk_smoke_test.py`.
2. Wire mode into usage text, argparse choices, help text, and dispatch.
3. Run the deterministic non-live smoke matrix including the new mode.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`

