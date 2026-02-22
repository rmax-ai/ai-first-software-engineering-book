# Recommended next task
Implement deterministic trace-summary observability in `state/kernel.py` and wire verification in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- The plan identifies observability as the highest-leverage harness capability for diagnosing loop behavior and evaluation outcomes.
- Adding deterministic trace summaries creates measurable signals that can be validated in smoke tests and consumed by eval checks.

## Acceptance criteria
- Add a deterministic trace-summary emission path in `state/kernel.py` that records loop-level metrics/events without changing existing public CLI behavior.
- Extend `state/copilot_sdk_uv_smoke.py` with at least one mode that asserts trace-summary presence and shape.
- Document expected regression signals and any required eval contract alignment in iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md`
- `state/feature_iterations/iter_002/04-validation.md`
