# Recommended next task

## Task
Implement deterministic trace logging controls in `state/kernel.py`.

## Why this is next
- It is the highest-value feature slice from this planning pass and improves harness observability.
- It creates concrete behavior to validate in smoke tests and eval contracts.

## Acceptance criteria
- Add a focused, minimal logging control path in `state/kernel.py` that emits deterministic trace entries for key loop stages.
- Add/adjust targeted verification in `state/copilot_sdk_uv_smoke.py` to assert expected trace signals.
- Update at least one relevant eval contract in `evals/*.yaml` so regressions in trace expectations are detectable.
- Record command evidence and pass/fail outcomes in the next iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (or another directly relevant `evals/*.yaml`)
