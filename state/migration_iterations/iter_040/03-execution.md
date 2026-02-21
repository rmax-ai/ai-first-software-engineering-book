# Execution

## Commands/tools run
- `apply_patch` to update `state/copilot_sdk_smoke_test.py` with `destroy-unavailable` mode coverage.
- `uv run python state/copilot_sdk_smoke_test.py --mode <mode>` loop across all deterministic non-live modes.

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added `run_destroy_unavailable_mode()` to exercise the non-callable `session.destroy` branch in `LLMClient.close()`.
- Updated usage docs and parser wiring so the new deterministic mode is discoverable and runnable.
