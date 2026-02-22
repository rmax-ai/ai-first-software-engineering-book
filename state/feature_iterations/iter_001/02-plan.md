# Plan

1. Review `DEVELOPMENT.md` and prompt constraints to align with harness governance and UV-first verification expectations.
2. Define feature-oriented backlog slices for:
   - richer trace observability in `state/kernel.py`
   - clearer role I/O structure in `state/role_io_templates.py`
   - deterministic harness controls and diagnostics surfaced through `state/` artifacts.
3. Define test work for each slice, including updates to `state/copilot_sdk_uv_smoke.py` and any targeted unit/smoke assets under `state/`.
4. Define eval integration work that maps feature changes to existing contracts under `evals/` and expected signals in harness metrics/outputs.
5. Record execution evidence and validation of this planning artifact set.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (only if metric schema/signals require updates)
