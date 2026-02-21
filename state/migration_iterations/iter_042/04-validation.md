# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-destroy-unavailable-close-idempotency`

## Observed outputs/results
- All listed deterministic non-live modes printed `PASS` and exited successfully.
- New mode output: `PASS: stop-destroy-unavailable-close-idempotency mode validates repeated close() after stop()/destroy() unavailable`.

## Pass/fail against acceptance criteria
- PASS: Added one deterministic combined mode for non-callable `stop()` and non-callable `destroy()`.
- PASS: First `close()` captured shutdown failure context (`stop() unavailable`) and second `close()` succeeded.
- PASS: Existing deterministic non-live smoke modes remained green.

