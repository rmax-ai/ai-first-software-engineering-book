# Next iteration recommendation

## Recommended task
Implement deterministic trace-summary contract updates in `state/kernel.py` and validate them with smoke coverage.

## Why this is next
- It is the highest-leverage feature from the seed plan and unlocks observable signals needed by both smoke tests and eval gates.
- Completing kernel trace shape first reduces rework in `state/copilot_sdk_uv_smoke.py` and `evals/*.yaml`.

## Acceptance criteria
- Add/adjust trace-summary fields in `state/kernel.py` with deterministic behavior.
- Add or update at least one smoke mode in `state/copilot_sdk_smoke_test.py` that fails on missing/invalid trace shape.
- Validate with `uv run python state/copilot_sdk_smoke_test.py --mode <new-or-updated-mode>`.
- Record evidence in `state/feature_iterations/iter_002/04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_smoke_test.py`
- `state/copilot_sdk_uv_smoke.py` (only if needed for trace plumbing)
