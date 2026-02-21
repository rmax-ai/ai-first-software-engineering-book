# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-destroy-unavailable-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-unavailable-close-idempotency`

## Observed outputs/results
- `PASS: stop-failure-destroy-unavailable-close-idempotency mode validates repeated close() after stop() failure and destroy() unavailable`
- `PASS: stub Copilot SDK path works`
- All deterministic non-live modes in the full matrix printed `PASS` and exited successfully.

## Pass/fail against acceptance criteria
- PASS: Added one deterministic mode forcing `stop()` failure plus non-callable `session.destroy()`.
- PASS: Mode verifies first `close()` reports `stop()=forced stop failure` and second `close()` succeeds.
- PASS: Existing deterministic non-live smoke modes remained green in a full matrix run.
