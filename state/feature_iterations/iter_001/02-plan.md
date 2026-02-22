# Plan

1. Review `DEVELOPMENT.md` and the seed prompt constraints to keep scope on harness planning only.
2. Define feature workstreams for `state/kernel.py` (trace logging/controls), `state/role_io_templates.py` (role I/O scaffolds), and deterministic execution guardrails.
3. Define test workstreams, prioritizing `uv run python state/copilot_sdk_uv_smoke.py` plus targeted unit/smoke additions under `state/`.
4. Define evaluation wiring to existing `evals/*.yaml` contracts and expected signals in `state/metrics.json`.
5. Record risks/decisions and select exactly one next implementation task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`
