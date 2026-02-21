# Execution

## Commands/tools run
- `view prompts/migration-iteration/execute.md`
- `view state/copilot-sdk-migration-plan.md`
- `view state/copilot_sdk_smoke_test.py`
- `apply_patch` on `state/copilot_sdk_smoke_test.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Added `run_close_idempotency_mode()` to assert first forced shutdown failure message contents and verify a second `close()` call is a no-op.
- Added CLI wiring (usage text, mode choices, dispatch) for `close-idempotency`.
