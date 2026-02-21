# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a dedicated mode for repeated `close()` after setting `session.destroy = None`.
2. Wire the new mode into usage text, argparse choices, help text, and dispatcher.
3. Run deterministic non-live smoke modes to verify no regressions.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
