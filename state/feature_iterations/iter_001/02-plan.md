# Plan

1. Review harness constraints from `DEVELOPMENT.md` and runner rules from `prompts/incremental-improvements/execute.md`.
2. Define feature backlog items for:
   - richer kernel trace observability in `state/kernel.py`
   - clearer and stricter role I/O scaffolding in `state/role_io_templates.py`
   - deterministic smoke/assertion expansion in `state/copilot_sdk_uv_smoke.py`
3. Define test strategy:
   - targeted UV smoke command(s) for changed harness surfaces
   - focused unit-style checks for helpers touched in `state/`
4. Define eval strategy tied to existing contracts:
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
5. Stage next iteration as a single minimal implementation task that touches one surface first (trace logging scaffolding in `state/kernel.py`) with bounded validation.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
