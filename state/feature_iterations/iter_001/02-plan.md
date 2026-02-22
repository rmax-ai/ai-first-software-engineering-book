# Plan

1. Baseline current guidance from `DEVELOPMENT.md` and `prompts/incremental-improvements/execute.md`.
2. Define feature backlog for deterministic harness improvements:
   - Add richer trace event schema and summary counters in `state/kernel.py`.
   - Clarify role input/output template contracts in `state/role_io_templates.py`.
   - Add deterministic smoke cases and failure-mode probes in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy:
   - Add/extend focused unit coverage for parser/validator helpers touched by kernel tracing work.
   - Add or update UV smoke modes that assert event ordering, budget accounting, and failure visibility.
4. Define evaluation strategy:
   - Map each new behavior to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, or `evals/drift-detection.yaml` checks.
   - Specify expected metric/ledger signals in `state/metrics.json` and iteration validation notes.
5. Sequence implementation across future single-task iterations with minimal diffs and targeted validations.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Targeted tests under `state/` and/or `book/` where needed
