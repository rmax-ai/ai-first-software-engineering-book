# Plan

1. Review governance and development constraints from `AGENTS.md` and `DEVELOPMENT.md`.
2. Define a feature backlog for deterministic harness improvements:
   - richer trace/decision observability in `state/kernel.py`
   - clearer role I/O template contracts in `state/role_io_templates.py`
   - deterministic smoke coverage extensions in `state/copilot_sdk_uv_smoke.py`
3. Map each feature area to validation:
   - targeted smoke command(s) using `uv run python ...`
   - eval contract checks tied to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
4. Document risks, trade-offs, and one smallest next implementation task with bounded scope.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
