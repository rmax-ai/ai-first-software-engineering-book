# Plan

1. Review `DEVELOPMENT.md` and existing `state/` harness surfaces to ground priorities.
2. Define feature improvements for deterministic execution, observability, and role-IO clarity:
   - `state/kernel.py`
   - `state/role_io_templates.py`
3. Define verification work:
   - expand `state/copilot_sdk_uv_smoke.py`
   - add/adjust targeted checks in `state/copilot_sdk_smoke_test.py`
4. Define regression gates and eval alignment:
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
   - `state/metrics.json` expected signal checks
5. Output one smallest next implementation task for iter_002 with clear acceptance criteria.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
