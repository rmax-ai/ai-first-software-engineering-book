# Next Iteration Recommendation

## Recommended next task
Implement deterministic trace-summary checkpoints in `state/kernel.py` and cover them with targeted smoke validation.

## Why this is next
Trace-summary visibility is the highest leverage foundation for subsequent template and eval work; it reduces debugging ambiguity and provides measurable regression signals.

## Acceptance criteria
- `state/kernel.py` emits structured trace-summary checkpoints for key loop phases and terminal outcomes.
- `state/copilot_sdk_uv_smoke.py` includes at least one deterministic mode that validates new trace-summary shape/fields.
- Validation evidence includes one targeted command run and observed pass/fail output recorded in iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
