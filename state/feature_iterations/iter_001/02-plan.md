# Plan

## Step-by-step
1. Baseline harness governance and workflow constraints from `DEVELOPMENT.md`.
2. Define feature improvements for later execution:
   - richer trace logging structure in `state/kernel.py` for deterministic loop visibility,
   - clearer role I/O scaffolds and constraints in `state/role_io_templates.py`,
   - stronger smoke coverage shape in `state/copilot_sdk_uv_smoke.py`.
3. Define validation strategy for each feature area with `uv run` commands and focused assertions.
4. Map regression gates to existing eval contracts in:
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
5. Capture one concrete next implementation task with acceptance criteria and expected file touchpoints.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/feature_iterations/iter_XXX/*.md`
