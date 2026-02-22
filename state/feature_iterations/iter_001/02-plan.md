# Plan

1. Inspect governance and development guidance (`DEVELOPMENT.md`) to anchor harness expectations around determinism, UV execution, and eval contracts.
2. Define a feature backlog for the harness:
   - `state/kernel.py`: richer trace checkpoints, deterministic budget accounting visibility, and clearer failure categorization.
   - `state/role_io_templates.py`: explicit role I/O schemas and stricter template validation helpers.
   - `state/copilot_sdk_uv_smoke.py`: targeted smoke scenarios for trace integrity and failure-surface coverage.
3. Define test strategy for each feature:
   - Add/extend kernel-focused unit tests for pure helpers.
   - Extend UV smoke coverage with deterministic pass/fail assertions.
   - Keep command surface centered on `uv run python ...` workflows.
4. Define evaluation strategy:
   - Map harness changes to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` checks.
   - Specify expected regression signals (metric drift, missing headings, style violations) and where they should be observed.
5. Record risks, trade-offs, and deferred items so execution iterations stay minimal and verifiable.
6. Recommend exactly one next iteration implementation task with bounded acceptance criteria.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/feature_iterations/iter_XXX/*.md`
