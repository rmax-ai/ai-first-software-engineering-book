# Plan

1. Define feature-plan scope for deterministic harness improvements:
   - richer trace and decision observability in `state/kernel.py`
   - clearer role I/O templates in `state/role_io_templates.py`
   - stronger smoke coverage in `state/copilot_sdk_uv_smoke.py`
2. Map each planned feature to validation:
   - targeted smoke/unit checks using `uv run python ...`
   - eval contract checks in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
3. Create a single, smallest next implementation task that can be executed in one future iteration with measurable acceptance criteria.
4. Record execution and validation evidence for this planning-only iteration.

## Expected files to change in this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
