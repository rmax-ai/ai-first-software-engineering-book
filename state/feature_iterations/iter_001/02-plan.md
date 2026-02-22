# Iteration plan

1. Capture required harness feature themes: richer trace observability, deterministic execution controls, and clearer role I/O contracts.
2. Map each theme to specific files and likely modification surfaces:
   - `state/kernel.py`: trace summary schema, deterministic guards, budget/eval visibility.
   - `state/role_io_templates.py`: stricter role input/output scaffolds and validation hints.
   - `state/copilot_sdk_uv_smoke.py`: smoke assertions for new harness controls.
   - `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`: regression checks for new behaviors.
3. Define test strategy for future implementation iterations:
   - targeted smoke modes via `uv run python state/copilot_sdk_uv_smoke.py ...`;
   - focused kernel verification commands using `uv run python state/kernel.py --chapter-id <id>`;
   - any added deterministic/unit checks for new pure helpers.
4. Define evaluation strategy:
   - tie each planned behavior to an eval signal or metric,
   - verify `state/metrics.json` receives expected indicators,
   - ensure iteration artifacts record command evidence.
5. Produce this iteration’s execution, validation, risks, and next-step handoff docs.

## Files expected to change in this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
