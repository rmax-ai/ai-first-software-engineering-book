# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-failure-close-idempotency`
- Deterministic non-live matrix run covering:
  - `stub`, `sdk-unavailable`, `bootstrap-failure`, `shutdown-failure`
  - `stop-unavailable`, `destroy-unavailable`, `destroy-failure`
  - `force-stop-unavailable`, `force-stop-close-idempotency`, `stop-close-idempotency`
  - `close-idempotency`, `destroy-close-idempotency`, `destroy-unavailable-close-idempotency`
  - `stop-destroy-unavailable-close-idempotency`, `stop-failure-destroy-unavailable-close-idempotency`, `stop-failure-destroy-failure-close-idempotency`

## Observed outputs/results
- `PASS: stop-failure-destroy-failure-close-idempotency mode validates repeated close() after stop()/destroy() failures`
- Task-agent summary reported `17/17 modes passed` with no failures.

## Pass/fail against acceptance criteria
- PASS: Added deterministic dual-failure mode forcing both `stop()` and `session.destroy()` failures.
- PASS: First `close()` asserts both error details are present; second `close()` remains idempotent.
- PASS: Deterministic non-live smoke matrix remained green.
