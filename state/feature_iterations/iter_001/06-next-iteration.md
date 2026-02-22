# Recommended next iteration

## Task
Implement deterministic trace-summary instrumentation in `state/kernel.py` and thread corresponding shape guards into `state/copilot_sdk_uv_smoke.py`.

## Why next
It is the smallest high-impact feature from the plan: it improves observability and creates immediately testable behavior with limited surface area.

## Acceptance criteria
- Add trace-summary payload emission in `state/kernel.py` without changing public CLI contract.
- Add/adjust deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py` to validate trace-summary structure.
- Update any affected eval expectations in `evals/*.yaml` only if required by new observable output.
- Record verification evidence from targeted `uv run python ...` commands.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (only if needed)
- `evals/drift-detection.yaml` (only if needed)
