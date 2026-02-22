# Plan

1. Reconfirm governance and engineering constraints from `DEVELOPMENT.md` for harness work in `state/`.
2. Define a feature backlog for later iterations:
   - Kernel observability and deterministic trace outputs in `state/kernel.py`.
   - Role I/O scaffold tightening in `state/role_io_templates.py`.
   - Stronger smoke coverage and scenario matrix updates in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy for each backlog item, prioritizing deterministic `uv run python ...` harness checks.
4. Define eval integration strategy for `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Capture risks, sequencing, and one next actionable implementation task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Targeted harness tests under `state/` and/or `book/` as needed
