# Plan

1. Capture target feature improvements for the harness:
   - richer trace/loop observability in `state/kernel.py`
   - clearer structured role I/O scaffolds in `state/role_io_templates.py`
   - deterministic smoke coverage updates in `state/copilot_sdk_uv_smoke.py`
2. Define validation updates:
   - map feature changes to targeted smoke/unit checks in `state/`
   - identify eval contract updates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
3. Sequence future execution:
   - implement observability plumbing first
   - extend smoke and eval assertions second
   - then document/verify via iteration artifacts.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
