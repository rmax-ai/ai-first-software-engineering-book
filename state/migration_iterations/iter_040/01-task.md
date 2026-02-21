# Task

## Selected task title
Add deterministic smoke coverage for non-callable `session.destroy()` shutdown behavior.

## Why this task now
`state/migration_iterations/iter_039/06-next-iteration.md` identified this as the next smallest uncovered shutdown branch.

## Acceptance criteria for this iteration
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `session.destroy` to non-callable, calls `close()`, and asserts expected shutdown behavior.
- Keep existing `destroy-failure` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.
