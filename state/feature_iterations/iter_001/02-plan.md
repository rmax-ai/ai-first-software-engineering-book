# Plan

1. Reconfirm harness constraints from `DEVELOPMENT.md` and the seed requirements in `prompts/incremental-improvements/execute.md`.
2. Define feature backlog items for deterministic harness behavior and observability:
   - richer phase/trace summaries in `state/kernel.py`
   - clearer structured role scaffolds in `state/role_io_templates.py`
   - stricter smoke-mode coverage and malformed-payload guards in `state/copilot_sdk_uv_smoke.py`
3. Define validation tests for each feature area:
   - targeted UV smoke commands (`uv run python state/copilot_sdk_uv_smoke.py --mode ...`)
   - focused kernel execution checks (`uv run python state/kernel.py --chapter-id <id>`)
4. Define evaluation wiring updates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` to detect regressions caused by harness changes.
5. Record risks, trade-offs, and one concrete next implementation task to execute in the next iteration.

## Files expected to change (this iteration)
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
