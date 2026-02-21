# Plan

1. Extend smoke test mode docs/CLI choices with `stop-unavailable`.
2. Add a deterministic mode that patches SDK client `stop` to be unavailable.
3. Verify expected `LLMClientError` message fragments.
4. Run targeted smoke commands for all required deterministic modes.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_033/*.md`
