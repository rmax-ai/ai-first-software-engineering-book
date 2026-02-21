# Validation

## Verification commands run
- `python state/copilot_sdk_smoke_test.py --mode stop-unavailable-destroy-failure-close-idempotency`
- Deterministic non-live matrix run covering:
  - `stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`
  - `stop-unavailable`, `destroy-unavailable`, `destroy-failure`
  - `force-stop-unavailable`, `force-stop-close-idempotency`, `stop-close-idempotency`
  - `close-idempotency`, `destroy-close-idempotency`, `destroy-unavailable-close-idempotency`
  - `stop-destroy-unavailable-close-idempotency`, `stop-unavailable-destroy-failure-close-idempotency`
  - `stop-failure-destroy-unavailable-close-idempotency`, `stop-failure-destroy-failure-close-idempotency`

## Observed outputs/results
- `PASS: stop-unavailable-destroy-failure-close-idempotency mode validates repeated close() after stop() unavailable and destroy() failure`
- Matrix run produced PASS for all 17 listed deterministic non-live modes.

## Pass/fail against acceptance criteria
- PASS: Added deterministic mode that sets `stop()` non-callable and forces `session.destroy()` failure.
- PASS: First `close()` asserts both `stop() unavailable` and `session.destroy()=forced destroy failure`.
- PASS: Second `close()` succeeds and deterministic non-live matrix stayed green.
