# Execution

## Commands/tools run
- `view state/copilot_sdk_smoke_test.py`
- `apply_patch` on `state/copilot_sdk_smoke_test.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Added `_init_shutdown_mode_client(user_prompt)` to centralize deterministic stub setup + warmup chat for shutdown-mode tests.
- Added `_teardown_shutdown_mode_client(client)` to centralize cleanup of SDK session/client loop state.
- Updated four shutdown-related test modes to reuse helpers without changing assertions.
