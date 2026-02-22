# Recommended next iteration

## Next task (exactly one)
Implement deterministic trace logging envelopes in `state/kernel.py` and add smoke coverage in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
This provides the smallest implementation slice from the plan that immediately improves observability and creates executable proof for future harness controls.

## Acceptance criteria
- Add deterministic trace envelope emission points in kernel execution flow with stable field names.
- Add/extend one smoke mode in `state/copilot_sdk_uv_smoke.py` that asserts trace envelope presence and structure.
- Update iteration artifacts with executed validation command output from `uv run python state/copilot_sdk_uv_smoke.py`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
