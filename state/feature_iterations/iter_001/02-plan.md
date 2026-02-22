# Iteration plan

1. Inventory current harness seams in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
2. Specify feature backlog: richer trace logging, explicit role I/O observability scaffolds, and deterministic execution controls.
3. Map each feature to verification: smoke mode additions in `state/copilot_sdk_uv_smoke.py` plus targeted kernel unit-style checks.
4. Map each feature to eval protection using `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
5. Define implementation order for future iterations with smallest-first diffs and explicit acceptance criteria.

## Expected files for later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (verification signal checks)
