# Plan

## Step-by-step

1. Baseline the current harness architecture and constraints from `DEVELOPMENT.md`.
2. Define the next feature backlog for deterministic harness behavior:
   - richer per-loop trace summaries and guard logging in `state/kernel.py`
   - clearer role I/O scaffolds and invariants in `state/role_io_templates.py`
   - deterministic smoke coverage extensions in `state/copilot_sdk_uv_smoke.py`
3. Define test strategy for each feature:
   - deterministic smoke modes run with `uv run python state/copilot_sdk_uv_smoke.py --mode ...`
   - focused Python tests for new pure helpers and parser/validator boundaries
   - command-level verification for kernel execution flow
4. Define evaluation gates and regression signals tied to:
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
   - state metric/ledger signals (for example `state/metrics.json` shape invariants).
5. Record one smallest recommended follow-up implementation task with bounded acceptance criteria.

## Expected files to change in future iterations

- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- relevant harness tests under `state/` and/or `book/`
