# Plan

1. Reconfirm harness contribution constraints from `DEVELOPMENT.md` and seed prompt requirements in `prompts/incremental-improvements/execute.md`.
2. Define feature workstreams for later iterations:
   - richer deterministic trace/decision visibility in `state/kernel.py`
   - clearer role-scaffold contracts in `state/role_io_templates.py`
   - stronger smoke/e2e harness controls in `state/copilot_sdk_uv_smoke.py`
3. Define verification workstreams:
   - targeted harness runs via `uv run python state/copilot_sdk_uv_smoke.py`
   - focused kernel checks via `uv run python state/kernel.py --chapter-id <id>`
   - optional unit-level parser/validator checks as gaps are found
4. Define evaluation integration workstreams:
   - map expected signals to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - ensure iteration validations capture metrics/ledger evidence in `state/metrics.json` and related artifacts
5. Write complete iteration artifacts and queue one concrete next implementation task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
