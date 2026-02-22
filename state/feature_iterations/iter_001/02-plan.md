# Iteration plan

1. Inspect `DEVELOPMENT.md` and current repository structure to anchor harness priorities.
2. Define feature backlog slices for `state/kernel.py` (trace logging, deterministic controls), `state/role_io_templates.py` (clearer role I/O templates), and supporting harness observability artifacts in `state/`.
3. Define test strategy around `state/copilot_sdk_uv_smoke.py` plus focused harness/unit scenarios that validate new controls.
4. Define eval integration points using `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`, including expected metric signals in `state/metrics.json`.
5. Publish one concrete next implementation task with acceptance criteria and explicit expected files.

## Files expected to change in later implementation iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`
