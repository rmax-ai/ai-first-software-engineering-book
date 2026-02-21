# Plan

1. Extend smoke test mode docs/CLI choices with `destroy-failure`.
2. Add a new deterministic mode that patches `session.destroy()` to raise.
3. Verify expected `LLMClientError` message fragments.
4. Run targeted smoke commands for all required modes.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_032/*.md`
