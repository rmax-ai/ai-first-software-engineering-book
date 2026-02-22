# Plan

1. Review `DEVELOPMENT.md` and extract harness constraints (UV workflow, deterministic guards, evidence requirements).
2. Define feature backlog themes:
   - richer kernel observability in `state/kernel.py`
   - clearer role scaffolds in `state/role_io_templates.py`
   - deterministic verification controls in `state/copilot_sdk_uv_smoke.py`
3. Define test strategy for each feature area using targeted `uv run python ...` smoke or unit-style harness checks.
4. Define evaluation strategy tying behavior to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Publish one concrete next implementation task with acceptance criteria and files to touch.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
