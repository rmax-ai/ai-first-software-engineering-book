# Execution

## Commands/tools run
- `uv run python state/copilot_sdk_smoke_test.py --mode <mode>` for baseline deterministic non-live modes.
- Edited `state/copilot_sdk_smoke_test.py` to add `force-stop-close-idempotency` mode and CLI wiring.
- `uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency`.
- `uv run python state/copilot_sdk_smoke_test.py --mode <mode>` for deterministic non-live regression coverage.

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Change rationale
- Added a focused deterministic mode to validate repeated `close()` behavior when `stop()` fails and `force_stop()` is unavailable.
- Kept existing `force-stop-unavailable` assertions/output unchanged to preserve prior branch semantics.
- Updated CLI mode surface so the new deterministic scenario is executable.
