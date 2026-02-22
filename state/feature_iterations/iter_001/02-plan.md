# Plan

1. Baseline current harness observability in `state/kernel.py` by cataloging emitted trace/metrics structures and identifying missing deterministic checkpoints.
2. Define a role-IO contract pass for `state/role_io_templates.py` to tighten schema consistency, required fields, and failure messaging for prompt scaffolds.
3. Expand deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py` with table-driven scenarios that validate the new checkpoints and role-IO invariants.
4. Align eval gates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` so regressions in trace shape, role scaffolds, and smoke behavior are caught.
5. Document expected metric and ledger impacts for each change so validation in future iterations is command-driven and repeatable.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
