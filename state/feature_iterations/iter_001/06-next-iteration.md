# Recommended next task

## Task
Implement structured trace logging and deterministic decision records in `state/kernel.py`.

## Why this is next
- It is the highest-value foundation item from this plan: better visibility makes later feature and eval changes safer and faster.
- It directly addresses current debugging and observability gaps without requiring a broad redesign.

## Acceptance criteria
- Add structured trace events for key loop decisions (task selection, verification result, stop/continue decision) in `state/kernel.py`.
- Ensure trace output is deterministic and can be validated in tests/smokes.
- Add targeted verification updates in `state/copilot_sdk_uv_smoke.py` that assert new trace signals.
- Document expected regression checks against `evals/chapter-quality.yaml` and `evals/drift-detection.yaml`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/drift-detection.yaml`
