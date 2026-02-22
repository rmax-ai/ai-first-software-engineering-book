# Recommended next task

## Task
Implement deterministic trace-summary observability enhancements in `state/kernel.py` and validate through smoke coverage.

## Why this is next
- The seed plan identifies kernel trace metadata as the highest-leverage dependency for downstream smoke and eval updates.
- Implementing this first creates concrete signals that `state/copilot_sdk_uv_smoke.py` and `evals/*.yaml` can assert.

## Acceptance criteria
1. `state/kernel.py` emits structured phase trace metadata for each major phase with stable keys.
2. `state/copilot_sdk_uv_smoke.py` adds/updates at least one mode that fails when required trace metadata is absent or malformed.
3. Validation run includes `uv run python state/copilot_sdk_uv_smoke.py --mode <new-or-updated-mode>` with pass/fail evidence recorded.
4. Iteration artifacts document any eval contract follow-up needed in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, or `evals/drift-detection.yaml`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py` (if matrix updates are required)
- `state/feature_iterations/iter_002/*`
