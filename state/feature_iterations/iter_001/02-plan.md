# Iteration plan

1. Review `DEVELOPMENT.md` and the seed prompt requirements to anchor scope to harness-only improvements.
2. Define feature backlog slices:
   - Add richer structured trace events and deterministic guard reporting in `state/kernel.py`.
   - Clarify/normalize role I/O scaffold contracts in `state/role_io_templates.py`.
   - Expand deterministic smoke scenarios in `state/copilot_sdk_uv_smoke.py` for newly introduced guardrails.
3. Define verification strategy:
   - Targeted smoke runs via `uv run python state/copilot_sdk_uv_smoke.py` modes tied to each feature slice.
   - Kernel-focused checks for guard behavior and ledger/metrics invariants.
4. Define eval integration strategy:
   - Map trace/guard changes to `evals/drift-detection.yaml` and `evals/style-guard.yaml` expectations.
   - Ensure chapter-quality signals remain compatible with `evals/chapter-quality.yaml`.
5. Record decisions, risks, and one recommended next implementation task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
