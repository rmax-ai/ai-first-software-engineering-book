# Plan

1. Extend `state/copilot_sdk_smoke_test.py` with a new deterministic `shutdown-failure` mode.
2. Patch the initialized SDK client's `stop()` and `force_stop()` methods in the smoke mode to force failures.
3. Assert shutdown error context and detailed stop/force_stop fragments.
4. Run targeted smoke modes: `stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
