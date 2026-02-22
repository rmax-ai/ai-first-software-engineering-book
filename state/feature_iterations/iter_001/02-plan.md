# Plan

1. Baseline current harness behavior and constraints from `DEVELOPMENT.md`, `state/kernel.py`, and existing smoke/eval assets.
2. Add deterministic trace-summary observability in `state/kernel.py`:
   - Emit stable per-step trace entries for planner/writer/critic + budget/eval checkpoints.
   - Keep output schema explicit so regressions are detectable.
3. Tighten role I/O scaffolds in `state/role_io_templates.py`:
   - Normalize expected headings/sections for each role.
   - Add validation hooks to fail fast on malformed role outputs.
4. Expand harness smoke coverage in `state/copilot_sdk_uv_smoke.py`:
   - Add deterministic modes that assert trace schema and role-output guards.
   - Keep CLI mode list table-driven for discoverability.
5. Wire eval protection in `evals/*.yaml`:
   - Add/adjust checks that confirm trace completeness and required chapter quality/style gates.
   - Ensure failures surface clear, actionable messages.
6. Validate each implementation slice using `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` plus targeted kernel invocations.
7. Record outcomes in each future iteration folder (`03-execution.md` and `04-validation.md`) and keep one scoped task per iteration.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
