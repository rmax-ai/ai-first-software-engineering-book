# Execution

## Commands/tools run
- `uv run python state/copilot_sdk_smoke_test.py --mode <mode>` for baseline deterministic modes.
- Edited `state/copilot_sdk_smoke_test.py` to add `stop-close-idempotency` mode.
- `uv run python state/copilot_sdk_smoke_test.py --mode <mode>` for deterministic modes including the new mode.

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Change rationale
- Added a focused deterministic mode to validate repeated `close()` behavior when `stop()` is unavailable.
- Kept `stop-unavailable` assertions/output unchanged to preserve prior coverage semantics.
- Updated CLI mode surface so the new deterministic scenario is runnable.
