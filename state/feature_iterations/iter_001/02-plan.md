# Plan

1. Audit current harness responsibilities in `state/kernel.py` to map control-flow hotspots (budgeting, guardrail checks, ledger/metrics writes).
2. Add deterministic trace expansion design in `state/kernel.py` (structured loop-step events, bounded payload fields, and explicit failure reason codes).
3. Define role-IO scaffold hardening updates in `state/role_io_templates.py` (consistent role contracts, strict section markers, and schema-level validation helpers).
4. Specify smoke-test growth in `state/copilot_sdk_uv_smoke.py` for new trace and scaffold invariants.
5. Identify eval contract adjustments in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` to catch regressions introduced by harness changes.
6. Document implementation order for follow-up iterations: trace events first, role-IO validation second, eval wiring third.

## Files expected to change in follow-up work
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
