# Plan

1. Baseline current harness touchpoints from `DEVELOPMENT.md` and existing `state/` assets.
2. Define feature backlog slices for:
   - richer kernel trace observability in `state/kernel.py`
   - clearer deterministic role I/O scaffolding in `state/role_io_templates.py`
   - stronger smoke coverage in `state/copilot_sdk_uv_smoke.py`
3. Map each feature slice to explicit tests and smoke commands (`uv run python ...`) needed for proof.
4. Map each slice to regression detection through `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`, including expected signals in `state/metrics.json`.
5. Produce a one-task next-iteration recommendation with concrete acceptance criteria and file targets.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (signal verification only; schema preserved)
