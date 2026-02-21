# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency`

## Observed outputs/results
- `PASS: stub Copilot SDK path works`
- `PASS: copilot provider requires SDK when module is unavailable`
- `PASS: bootstrap failure mode validates worker-loop bootstrap error context`
- `PASS: shutdown failure mode validates stop()/force_stop() error context`
- `PASS: stop unavailable mode validates stop() unavailable shutdown error context`
- `PASS: destroy failure mode validates session.destroy() error context`
- `PASS: force-stop-unavailable mode validates force_stop() unavailable shutdown error context`
- `PASS: close-idempotency mode validates repeated close() after shutdown failure`
- `PASS: destroy-close-idempotency mode validates repeated close() after destroy failure`

## Pass/fail against acceptance criteria
- Added deterministic destroy-failure idempotency mode: **pass**.
- Verified first `close()` raises with destroy detail and second `close()` does not raise: **pass**.
- Preserved existing `destroy-failure` behavior and deterministic mode pass status: **pass**.
