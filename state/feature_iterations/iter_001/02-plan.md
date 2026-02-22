# Plan

1. Inventory harness constraints from `DEVELOPMENT.md` and align plan scope to deterministic, minimal-diff iteration work.
2. Define feature backlog for `state/kernel.py` focused on deterministic execution controls and richer trace/decision observability.
3. Define role I/O scaffolding improvements for `state/role_io_templates.py` that tighten prompt/response structure and reduce ambiguity.
4. Define smoke-test expansion in `state/copilot_sdk_uv_smoke.py` for failure-mode and lifecycle regressions tied to new controls.
5. Map regression gates to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` so later changes have explicit evaluation targets.
6. Record risks/decisions and provide one smallest next implementation task with acceptance criteria.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
