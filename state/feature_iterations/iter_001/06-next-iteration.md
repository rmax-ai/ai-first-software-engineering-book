# Recommended next task

## Task
Implement kernel phase-trace observability primitives in `state/kernel.py`.

## Why next
- Kernel trace primitives are the foundation for smoke and eval assertions planned in this seed iteration.

## Acceptance criteria
- Add deterministic phase-trace entries for planner/writer/critic execution phases.
- Persist trace payloads in the existing harness output path without changing public CLI flags.
- Add focused verification command(s) proving trace entries exist and are schema-valid.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
