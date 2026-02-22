# Plan

1. Review harness guidance in `DEVELOPMENT.md` and align the planning scope to `state/` components.
2. Define feature backlog items for:
   - deterministic execution controls in `state/kernel.py`
   - richer role/IO scaffolding in `state/role_io_templates.py`
   - stronger smoke observability in `state/copilot_sdk_uv_smoke.py`
3. Map each feature item to targeted verification commands and expected evidence artifacts.
4. Map each feature item to eval gates under `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Record risks, trade-offs, and one concrete next implementation task.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
