# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when `stop()` is unavailable.

## Why this task now
`state/migration_iterations/iter_037/06-next-iteration.md` prioritized this as the next smallest untested shutdown-hardening branch.

## Acceptance criteria for this iteration
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `stop` to non-callable, calls `close()` twice, and asserts only the first call raises.
- Keep existing `stop-unavailable` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.
