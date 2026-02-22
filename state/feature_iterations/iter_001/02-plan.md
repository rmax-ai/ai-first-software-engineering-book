# Iteration plan (planning-only)

1. Baseline current harness governance and execution constraints from `DEVELOPMENT.md`.
2. Define feature backlog slices for:
   - richer kernel observability in `state/kernel.py`
   - clearer role I/O scaffolds in `state/role_io_templates.py`
   - deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py`
3. Map each feature slice to concrete validation:
   - targeted `uv run python ...` harness commands
   - eval contract checks in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
4. Sequence the first executable task as a minimal, testable follow-up iteration.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
