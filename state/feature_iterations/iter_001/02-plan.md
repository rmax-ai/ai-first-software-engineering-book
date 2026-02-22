# Iteration plan

1. Audit current harness touchpoints in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py` to anchor realistic improvements.
2. Define feature backlog items with explicit expected behavior:
   - richer trace logging and run summaries in `state/kernel.py`
   - clearer role-input/output template contracts in `state/role_io_templates.py`
   - deterministic smoke controls and assertions in `state/copilot_sdk_uv_smoke.py`
3. Define test strategy for each item:
   - targeted unit tests for pure helper behavior
   - `uv run python state/copilot_sdk_uv_smoke.py` modes for deterministic integration coverage
4. Define evaluation wiring:
   - map improvements to existing eval contracts in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - define expected `state/metrics.json` or trace-signal deltas that prove regression resistance
5. Stage implementation order for future iterations: logging foundation first, role-IO normalization second, smoke/eval tightening third.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- related harness tests under `state/` and/or `book/`
