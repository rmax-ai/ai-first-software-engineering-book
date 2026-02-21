# Execution

## Commands/tools run
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add mode and assertions.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added a deterministic destroy-failure path to validate `session.destroy()` error aggregation in shutdown handling.
- Updated mode documentation and CLI routing so the scenario is executable via `--mode destroy-failure`.
