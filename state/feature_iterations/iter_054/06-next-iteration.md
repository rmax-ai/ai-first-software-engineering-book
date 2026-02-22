# Next iteration

## Recommended next task
Implement phase-level structured trace logging in `state/kernel.py` and validate it through `state/copilot_sdk_uv_smoke.py`.

## Why it is next
Structured observability is the first feature track from this planning iteration and enables clearer verification for subsequent scaffold and execution-control improvements.

## Concrete acceptance criteria
1. Add deterministic phase-level trace fields (phase name, status, duration/budget signal) in `state/kernel.py` without changing public CLI behavior.
2. Add/update smoke coverage in `state/copilot_sdk_uv_smoke.py` to assert the new trace signal shape.
3. Run targeted validation:
   - `uv run python state/copilot_sdk_uv_smoke.py`
   - one focused kernel execution command from `DEVELOPMENT.md` (for example: `uv run python state/kernel.py --chapter-id <id>`)

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_055/*.md`
