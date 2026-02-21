# Execution

## Commands/tools run
- Edited `state/copilot_sdk_smoke_test.py` to add a new deterministic mode.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added `force-stop-unavailable` mode to exercise the `close()` branch where `stop()` fails and `force_stop()` is unavailable.
- Added assertions that shutdown failures include both the prefix and unavailable `force_stop()` detail.
- Wired new mode into CLI parser choices/help and dispatch.
