# Plan

1. Define kernel feature backlog in `state/kernel.py`:
   - add structured phase-trace emission points,
   - add deterministic loop budget observability counters,
   - expose a strict failure reason map for stop conditions.
2. Define role scaffold improvements in `state/role_io_templates.py`:
   - tighten role I/O contract sections,
   - normalize required headings for deterministic downstream validation.
3. Define smoke coverage expansion in `state/copilot_sdk_uv_smoke.py`:
   - add table-driven modes for new trace/contract guard paths,
   - add explicit negative-path fixtures for malformed trace payloads.
4. Define eval wiring updates in `evals/*.yaml`:
   - map new observability/failure signals to chapter-quality and drift gates,
   - ensure eval expectations reference deterministic trace artifacts.
5. Sequence later iterations:
   - iteration A: kernel observability primitives,
   - iteration B: role scaffold contract alignment,
   - iteration C: smoke/eval regression gates and final verification.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
