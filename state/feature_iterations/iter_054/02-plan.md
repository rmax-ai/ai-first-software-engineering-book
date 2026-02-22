# Plan

1. Inventory current harness touchpoints in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` to anchor improvements to existing behavior.
2. Define a feature backlog with three concrete tracks:
   - richer kernel observability (structured phase-level trace details and deterministic counters),
   - clearer role I/O scaffold contracts (template metadata and prompt-shape checks),
   - deterministic execution controls (explicit budget/eval guard reporting).
3. Define test coverage for each feature track:
   - targeted kernel unit coverage for parsing/validation helpers,
   - smoke updates in `state/copilot_sdk_uv_smoke.py` that assert new trace and contract signals,
   - deterministic command checks using `uv run python ...` entrypoints from `DEVELOPMENT.md`.
4. Define eval integration updates for regression detection:
   - map each planned feature to at least one existing or updated eval contract in `evals/`,
   - ensure expected telemetry aligns with `state/metrics.json` and iteration artifacts.
5. Sequence future iterations as smallest shippable steps: observability first, scaffold checks second, deterministic controls third, then eval hardening and cleanup.

## Files expected to change
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
