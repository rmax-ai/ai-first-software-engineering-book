# Plan

1. Inventory current harness touchpoints from `DEVELOPMENT.md` to anchor the backlog around:
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
   - `evals/*.yaml`
2. Define feature backlog items for determinism and observability:
   - structured trace logging boundaries in kernel flow,
   - clearer role IO scaffold contracts,
   - deterministic execution constraints and error surfacing.
3. Define test backlog items:
   - expand smoke assertions in `state/copilot_sdk_uv_smoke.py`,
   - add targeted kernel helper coverage for trace/constraint behavior,
   - add fixture-based checks for role IO template expectations.
4. Define evaluation backlog items:
   - map feature/test changes to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`,
   - identify expected telemetry/metrics confirmations in `state/metrics.json`.
5. Sequence implementation into future single-task iterations, each with one narrow acceptance target and explicit file list.

## Files expected to change in later iterations

- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (only if metric schema/signals need updates)
