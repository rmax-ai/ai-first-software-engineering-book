# Plan

1. Inventory current harness entry points and constraints from `DEVELOPMENT.md` and existing files in `state/` and `evals/`.
2. Define a feature backlog for deterministic harness behavior:
   - richer trace events in `state/kernel.py`,
   - clearer role IO scaffolds in `state/role_io_templates.py`,
   - deterministic smoke controls in `state/copilot_sdk_uv_smoke.py`.
3. Define test backlog tied to each feature:
   - targeted `uv run python state/copilot_sdk_uv_smoke.py` modes,
   - focused unit-level checks around kernel helper boundaries,
   - fixture-driven checks for role IO template integrity.
4. Define evaluation backlog:
   - align new checks with `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`,
   - specify expected deltas in `state/metrics.json` and iteration evidence artifacts.
5. Sequence implementation into smallest future tasks (one behavior per iteration, each with targeted verification and artifact updates).

## Expected files for future implementation iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`

