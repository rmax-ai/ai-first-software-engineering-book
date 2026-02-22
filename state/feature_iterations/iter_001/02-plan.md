# Plan

1. Define feature workstreams for harness observability, deterministic controls, and role I/O scaffolding quality.
2. Break down follow-up implementation touchpoints in:
   - `state/kernel.py` (trace logging + deterministic constraints)
   - `state/role_io_templates.py` (clearer templates and validation hooks)
   - `state/copilot_sdk_uv_smoke.py` (new smoke coverage for added controls)
   - `evals/*.yaml` (regression detection expectations aligned to new signals)
3. Specify test strategy:
   - `uv run python state/copilot_sdk_uv_smoke.py` mode additions
   - targeted kernel/unit checks for parser/constraint helpers
   - fixture-based checks for role template behavior
4. Specify evaluation strategy:
   - map new behavior to existing eval contracts
   - define expected metric/ledger signals and failure criteria
5. Document one smallest next implementation task with explicit acceptance criteria.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (only if expected signals change)
