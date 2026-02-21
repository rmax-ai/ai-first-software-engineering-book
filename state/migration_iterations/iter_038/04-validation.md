# Validation

## Verification commands run
- `for mode in stub sdk-unavailable bootstrap-failure shutdown-failure stop-unavailable destroy-failure force-stop-unavailable close-idempotency destroy-close-idempotency; do uv run python state/copilot_sdk_smoke_test.py --mode "$mode"; done`
- `for mode in stub sdk-unavailable bootstrap-failure shutdown-failure stop-unavailable destroy-failure force-stop-unavailable stop-close-idempotency close-idempotency destroy-close-idempotency; do uv run python state/copilot_sdk_smoke_test.py --mode "$mode"; done`

## Observed outputs/results
- Baseline deterministic run passed all pre-existing non-live modes.
- Post-change deterministic run passed all non-live modes, including `stop-close-idempotency`.
- `stop-unavailable` mode continues to print: `PASS: stop unavailable mode validates stop() unavailable shutdown error context`.

## Acceptance criteria status
- Added deterministic stop-unavailable close-idempotency mode: **PASS**.
- Preserved existing stop-unavailable assertions/output: **PASS**.
- All deterministic non-live modes passing: **PASS**.
