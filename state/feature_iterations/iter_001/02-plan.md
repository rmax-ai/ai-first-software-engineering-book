# Plan

1. Confirm governance and harness guidance from `DEVELOPMENT.md`.
2. Define a compact backlog for harness improvements with three lanes:
   - **Features**: deterministic trace/phase observability, role-IO scaffold clarity, and stronger execution controls in kernel flow.
   - **Tests**: smoke and targeted script checks proving each added behavior.
   - **Evals**: explicit mapping from behavior to `evals/*.yaml` and expected signal changes.
3. Write iteration artifacts documenting the above so future iterations can implement one smallest item at a time.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
