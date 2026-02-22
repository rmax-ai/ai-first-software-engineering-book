# Plan

1. Review harness guidance in `DEVELOPMENT.md` and align backlog items with `state/` architecture constraints.
2. Define feature work for `state/kernel.py`:
   - richer per-step trace summaries,
   - deterministic execution-budget diagnostics,
   - explicit failure classification for eval-gate exits.
3. Define role-IO scaffolding work in `state/role_io_templates.py`:
   - clearer role handoff contracts,
   - stricter prompt-shape validation helpers.
4. Define verification harness work in `state/copilot_sdk_uv_smoke.py`:
   - add targeted smoke modes for new diagnostics and trace outputs.
5. Define eval wiring work in `evals/*.yaml`:
   - map new behavior to measurable gates,
   - align expected output signals with `state/metrics.json` fields.
6. Capture sequencing for follow-up iterations:
   - implement kernel observability first,
   - then role-IO constraints,
   - then smoke coverage and eval-gate updates.

## Expected files in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`
