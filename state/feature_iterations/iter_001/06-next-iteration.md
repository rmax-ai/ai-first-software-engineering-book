# Next iteration recommendation

## Recommended next task
Implement deterministic phase-trace summary validation in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- It directly operationalizes the planning focus on observability and deterministic guards.
- It is small, measurable, and provides immediate regression detection value.

## Acceptance criteria
1. Add one new smoke mode that fails when required `phase_trace` content is missing or malformed.
2. Ensure mode registration is table-driven and appears in argparse help/choices.
3. Add/adjust deterministic smoke tests in `state/copilot_sdk_smoke_test.py` for the new mode.
4. Run targeted verification:
   - `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`
   - `uv run python state/copilot_sdk_smoke_test.py`

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_002/0*.md`
