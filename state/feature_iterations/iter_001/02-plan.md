# Plan

1. Inspect governance and development guidance (`DEVELOPMENT.md`) plus current harness surfaces in `state/` and eval contracts in `evals/*.yaml`.
2. Define feature backlog themes for:
   - `state/kernel.py` (traceability, deterministic controls, clearer failure signals)
   - `state/role_io_templates.py` (role scaffold consistency and debuggability)
   - `state/copilot_sdk_uv_smoke.py` (smoke coverage for new harness behaviors)
3. Define test strategy:
   - deterministic smoke command(s): `uv run python state/copilot_sdk_uv_smoke.py`
   - targeted unit-style harness checks in `state/` for helper-level behavior
4. Define evaluation strategy mapping to existing eval contracts:
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
5. Capture risks, decisions, and one concrete next implementation task.

## Expected files to change
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
