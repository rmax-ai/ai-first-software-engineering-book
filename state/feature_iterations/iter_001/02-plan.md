# Plan

1. Confirm harness constraints and workflows from `DEVELOPMENT.md` and prompt contract.
2. Define feature backlog slices for deterministic controls and observability:
   - extend trace/evidence structure in `state/kernel.py`
   - clarify role scaffolds in `state/role_io_templates.py`
   - tighten smoke coverage in `state/copilot_sdk_uv_smoke.py`
3. Define test work for each slice using `uv run python ...` commands and targeted deterministic checks.
4. Define eval wiring updates by mapping changed behavior to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Sequence implementation into smallest tasks with one-task-per-iteration handoff.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
