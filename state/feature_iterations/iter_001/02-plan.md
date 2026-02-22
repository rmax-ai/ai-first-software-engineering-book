# Single-task plan

1. Inspect the execution contract in `prompts/incremental-improvements/execute.md` and harness constraints in `DEVELOPMENT.md`.
2. Capture a feature backlog for deterministic harness improvements:
   - Add richer trace summaries and guard metadata emission in `state/kernel.py`.
   - Tighten role IO scaffolds and validation helpers in `state/role_io_templates.py`.
   - Expand deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py`.
3. Define the test strategy for each feature:
   - Targeted uv smoke modes (`uv run python state/copilot_sdk_uv_smoke.py --mode ...`).
   - Focused unit/contract checks for template and trace-shape guards.
4. Define evaluation wiring and regression detection:
   - Map harness behavior to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Require recorded validation signals in iteration artifacts and `state/metrics.json` deltas when behavior changes.
5. Publish all seven iteration artifacts in `state/feature_iterations/iter_001/` and recommend exactly one next implementation task.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
