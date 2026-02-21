# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency after `session.destroy()` failure.

## Why this task now
`state/migration_iterations/iter_036/06-next-iteration.md` prioritized destroy-specific idempotency to complete the next smallest M2 shutdown-hardening branch.

## Acceptance criteria for this iteration
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that forces `session.destroy()` failure.
- Call `close()` twice and assert only the first call raises.
- Preserve existing `destroy-failure` assertions and pass output.
