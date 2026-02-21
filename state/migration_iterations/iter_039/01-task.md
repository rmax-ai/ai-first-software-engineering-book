# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when `force_stop()` is unavailable.

## Why this task now
`state/migration_iterations/iter_038/06-next-iteration.md` marked this as the next smallest uncovered shutdown-hardening branch.

## Acceptance criteria for this iteration
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `stop()` to fail and `force_stop` to non-callable, calls `close()` twice, and asserts only the first call raises.
- Keep existing `force-stop-unavailable` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.
