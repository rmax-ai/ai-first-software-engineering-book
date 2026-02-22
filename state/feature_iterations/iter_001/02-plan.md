# Plan

1. Confirm this seed iteration is planning-only and scoped to one task.
2. Build a prioritized feature backlog for harness improvements:
   - richer trace logging and decision visibility in `state/kernel.py`
   - clearer role IO scaffolds in `state/role_io_templates.py`
   - deterministic control toggles and guardrails for kernel execution
3. Define verification work:
   - targeted smoke coverage in `state/copilot_sdk_uv_smoke.py`
   - focused kernel helper/unit checks for new deterministic behavior
4. Define eval/regression mapping:
   - map expected impacts to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - specify measurable success signals to monitor in `state/metrics.json`
5. Record execution, validation evidence, risks, and one concrete next task.

## Files expected to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
