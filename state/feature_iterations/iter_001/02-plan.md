# Iteration plan

1. Inventory current harness surfaces from `DEVELOPMENT.md` and existing `state/` + `evals/` contracts.
2. Define feature improvements for deterministic execution visibility and controllability:
   - structured phase-trace output and richer failure metadata in `state/kernel.py`.
   - clearer role-scaffold metadata and validation hooks in `state/role_io_templates.py`.
   - expanded smoke coverage modes in `state/copilot_sdk_uv_smoke.py` for trace and shutdown behaviors.
3. Define verification work:
   - targeted harness smoke runs with `uv run python state/copilot_sdk_uv_smoke.py`.
   - kernel-focused deterministic checks around trace payload shape and budget gates.
4. Define regression evaluation wiring:
   - map expected signals to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - ensure future implementation updates document impacts to `state/metrics.json`.
5. Publish this iteration’s artifacts and recommend one smallest next implementation task.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
