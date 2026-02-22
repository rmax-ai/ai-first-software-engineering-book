# Recommended next iteration task

## Task
Formalize kernel phase-trace schema and enforce payload validation.

## Why this is next
The plan depends on deterministic observability. A stable, validated phase-trace contract in `state/kernel.py` is the smallest enabling change for follow-on smoke and eval updates.

## Acceptance criteria
- Add explicit phase-trace schema validation in `state/kernel.py` for required fields and payload object shape.
- Ensure malformed/missing phase-trace entries produce deterministic failure signals.
- Extend `state/copilot_sdk_uv_smoke.py` with at least one targeted mode validating the new schema enforcement.
- Document expected regression signals impacting `evals/drift-detection.yaml`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/drift-detection.yaml`
