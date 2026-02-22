# Iteration plan

1. Define observability and control upgrades for the harness loop in `state/kernel.py`:
   - Structured per-loop self-evaluation capture.
   - Deterministic stop-state reporting when loop budget is exhausted.
   - Explicit evidence bookkeeping for verification commands and outcomes.
2. Plan clearer role-I/O boundaries in `state/role_io_templates.py`:
   - Template slots for plan/change/evaluate/decision phases.
   - Compact handoff fields that map to iteration artifacts.
3. Plan smoke and targeted test coverage in `state/copilot_sdk_uv_smoke.py` and nearby harness tests:
   - Add/extend deterministic modes that assert self-evaluation logging and stop-condition behavior.
   - Add table-driven checks for missing or malformed execution evidence.
4. Plan eval integration under `evals/`:
   - Identify/update YAML contracts that should gate harness regressions in structure, drift, and style.
   - Define expected signals that should align with `state/metrics.json` updates.
5. Sequence future iterations:
   - Implement one behavior slice at a time with minimal diffs.
   - Run targeted `uv run python ...` checks per slice and document evidence in each iteration folder.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Potential targeted harness test files under `state/`
