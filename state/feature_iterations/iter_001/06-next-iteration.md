# Recommended next task (exactly one)
Implement deterministic trace-summary observability in `state/kernel.py` and prove it through smoke coverage.

## Why this is next
- It is the highest-value first feature from the seed plan and enables clearer regression detection for subsequent harness changes.

## Acceptance criteria
- Add a focused kernel output path that emits a deterministic trace summary entry for each chapter run.
- Extend `state/copilot_sdk_uv_smoke.py` with at least one deterministic mode that validates summary shape/content.
- Update relevant eval contract(s) in `evals/*.yaml` so regressions fail predictably.
- Record verification evidence using `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (or another directly relevant eval file)
- `state/feature_iterations/iter_002/*`
