# Task

## Selected task title
Add deterministic smoke coverage for repeated `close()` idempotency when `session.destroy` is non-callable.

## Why this task now
`iter_040/06-next-iteration.md` prioritized this exact gap to complete shutdown hardening coverage for the non-callable `session.destroy` branch.

## Acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that sets `session.destroy` non-callable, calls `close()` twice, and asserts no exception on either call.
- Keep existing `destroy-unavailable` mode assertions and output text unchanged.
- Keep deterministic non-live smoke modes passing.
