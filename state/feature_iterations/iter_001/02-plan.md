# Iteration plan

1. Review `DEVELOPMENT.md` and extract constraints for UV usage, deterministic behavior, and evaluation gates.
2. Define feature backlog slices for harness observability, deterministic controls, and role-IO clarity, mapped to `state/kernel.py` and `state/role_io_templates.py`.
3. Define test backlog slices for deterministic and live harness checks in `state/copilot_sdk_uv_smoke.py` plus targeted harness tests under `state/`.
4. Define eval alignment work for `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` with expected regression signals and metric checks in `state/metrics.json`.
5. Capture execution evidence, validation outcomes, and risks in iteration artifacts.
6. Set one next task that starts implementation from the highest-value backlog item.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Additional targeted tests under `state/` as needed
