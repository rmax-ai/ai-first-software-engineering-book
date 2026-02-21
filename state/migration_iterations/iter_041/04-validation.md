# Validation

## Verification commands run
- `for mode in stub sdk-unavailable bootstrap-failure shutdown-failure stop-unavailable destroy-unavailable destroy-failure force-stop-unavailable force-stop-close-idempotency stop-close-idempotency close-idempotency destroy-close-idempotency destroy-unavailable-close-idempotency; do uv run python state/copilot_sdk_smoke_test.py --mode "$mode"; done`

## Observed outputs/results
- All listed modes printed `PASS` and exited successfully.
- New mode output: `PASS: destroy-unavailable-close-idempotency mode validates repeated close() after destroy() unavailable`.

## Pass/fail against acceptance criteria
- PASS: Added deterministic mode for non-callable `session.destroy` with two `close()` calls.
- PASS: Existing `destroy-unavailable` mode behavior/output remains unchanged.
- PASS: Deterministic non-live smoke modes pass.
