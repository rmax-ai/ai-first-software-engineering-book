# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency`
- `uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure && uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure && uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure && uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency && uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency`

## Observed outputs/results
- Baseline deterministic run passed all pre-existing non-live modes.
- New mode output: `PASS: force-stop-close-idempotency mode validates repeated close() after force_stop() unavailable`.
- Post-change deterministic run passed all non-live modes.
- Existing mode output remained unchanged: `PASS: force-stop-unavailable mode validates force_stop() unavailable shutdown error context`.

## Acceptance criteria status
- Added deterministic force-stop-unavailable close-idempotency mode: **PASS**.
- Preserved existing force-stop-unavailable assertions/output: **PASS**.
- All deterministic non-live modes passing: **PASS**.
