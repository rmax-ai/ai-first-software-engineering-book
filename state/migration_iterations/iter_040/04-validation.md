# Validation

## Verification commands run
- `for m in stub sdk-unavailable bootstrap-failure shutdown-failure stop-unavailable destroy-unavailable destroy-failure force-stop-unavailable force-stop-close-idempotency stop-close-idempotency close-idempotency destroy-close-idempotency; do uv run python state/copilot_sdk_smoke_test.py --mode "$m"; done`

## Observed outputs/results
- New mode output: `PASS: destroy unavailable mode validates non-callable session.destroy() shutdown success path`.
- Existing mode output unchanged: `PASS: destroy failure mode validates session.destroy() error context`.
- All deterministic non-live modes completed successfully.

## Acceptance criteria status
- Added deterministic `destroy-unavailable` mode with expected shutdown behavior assertion: **PASS**.
- Preserved existing `destroy-failure` assertions/output: **PASS**.
- All deterministic non-live modes passing: **PASS**.
