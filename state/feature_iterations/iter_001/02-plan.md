# Iteration plan (single task)

1. Review harness guidance in `DEVELOPMENT.md` and align scope to deterministic, minimal-surface harness changes.
2. Define feature backlog themes for:
   - richer trace observability in `state/kernel.py`
   - clearer role I/O scaffolding in `state/role_io_templates.py`
   - stronger deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py`
   - regression gates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
3. Map each theme to target verification commands (`uv run python ...`) and expected evidence artifacts.
4. Record risks/trade-offs and defer implementation to subsequent iterations.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
