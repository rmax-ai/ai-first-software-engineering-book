# Execution

## Commands/tools run
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add a new deterministic mode and CLI wiring.
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-unavailable-close-idempotency`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Change rationale
- Added `run_stop_failure_destroy_unavailable_close_idempotency_mode()` to cover the mixed path where `stop()` raises while `session.destroy()` is non-callable.
- Updated mode documentation and CLI parsing so the new deterministic mode is runnable like existing smoke modes.
