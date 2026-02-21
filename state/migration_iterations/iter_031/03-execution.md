# Execution

## Commands/tools run
- `view state/copilot_sdk_smoke_test.py`
- `view state/llm_client.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added `shutdown-failure` mode to deterministically trigger both `stop()` and `force_stop()` failures on the SDK client and verify `LLMClient.close()` raises `Copilot SDK shutdown failed:` with both failure details.
- Updated CLI mode choices/help and top-level usage/mode documentation for the new test path.
