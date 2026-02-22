# Next iteration task

## Recommended task
Implement deterministic trace-observability enhancements in `state/kernel.py` and wire smoke validation in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- The seed plan identified trace metadata and deterministic decision visibility as the highest-leverage feature gap.
- This unlocks measurable regression checks before broader template or evaluator extensions.

## Acceptance criteria
- Add explicit trace-summary fields for iteration decision context in `state/kernel.py` without changing existing public CLI arguments.
- Extend `state/copilot_sdk_uv_smoke.py` with one deterministic mode that asserts the new trace-summary shape.
- Update iteration validation artifacts with executed `uv run python state/copilot_sdk_uv_smoke.py --mode ...` evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
- `state/feature_iterations/iter_002/03-execution.md`
