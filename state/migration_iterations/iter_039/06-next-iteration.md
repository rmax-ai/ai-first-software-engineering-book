# Next Iteration

## Recommended next task
Add deterministic smoke coverage for `session.destroy()` unavailable shutdown behavior.

## Why it is next
Current shutdown coverage validates `session.destroy()` exceptions but does not explicitly validate the non-callable `session.destroy` branch.

## Concrete acceptance criteria
- Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that patches `session.destroy` to non-callable, calls `close()`, and asserts expected shutdown behavior.
- Keep existing `destroy-failure` mode assertions and output text unchanged.
- Keep all deterministic non-live modes passing.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
