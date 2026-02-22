# Plan

1. Define feature backlog slices for harness observability and execution controls in `state/kernel.py`.
2. Define role I/O contract hardening work in `state/role_io_templates.py` to keep scaffolds deterministic.
3. Define smoke-test expansion in `state/copilot_sdk_uv_smoke.py` for new harness controls.
4. Define eval coverage updates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Sequence future iterations as one smallest task each, with targeted validation per touched surface.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Related test fixtures under `state/` or `book/` if required by acceptance criteria.
