# Plan

1. Update `state/llm_client.py::_ensure_sdk_thread_loop` to use a startup timeout and explicit bootstrap failure paths.
2. Keep scope limited to worker-loop startup handling only.
3. Run deterministic smoke checks in `state/copilot_sdk_smoke_test.py` (`stub`, `sdk-unavailable`).

## Files expected to change
- `state/llm_client.py`
- `state/migration_iterations/iter_029/*.md`
