# Next iteration recommendation

## Recommended task
Add deterministic trace summary counters to `state/kernel.py` and expose them in smoke validation.

## Why this is next
- It is the smallest implementation step that improves observability without changing public harness interfaces.
- It creates measurable output that can be asserted in smoke and eval checks.

## Acceptance criteria
- Add a focused helper in `state/kernel.py` that emits stable trace counters for key loop outcomes.
- Update `state/copilot_sdk_uv_smoke.py` with one new targeted assertion mode that verifies the new trace counters.
- Run `uv run python state/copilot_sdk_uv_smoke.py` and record pass/fail evidence in iteration validation artifacts.
- Ensure no changes are required to user-facing CLI interfaces.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0{1..7}-*.md` (new iteration artifacts)
