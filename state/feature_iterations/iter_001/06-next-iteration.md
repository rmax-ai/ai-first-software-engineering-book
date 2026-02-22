# Next iteration recommendation

## Recommended task (exactly one)
Add deterministic trace-summary event emission in `state/kernel.py` for major harness phase transitions.

## Why this is next
- It is the smallest concrete feature that improves observability and can be validated without touching multiple systems at once.
- It creates a stable signal that later smoke and eval improvements can assert against.

## Acceptance criteria
1. `state/kernel.py` emits a structured trace-summary event at each major phase boundary (planning, execution, validation, handoff).
2. Event schema is documented and deterministic (stable keys/order and bounded values).
3. A targeted harness check verifies presence and shape of the new events.
4. Iteration artifacts include command evidence and pass/fail outcomes.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/`

