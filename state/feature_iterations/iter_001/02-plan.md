# Plan

1. Audit current harness seams in `state/kernel.py` to identify deterministic guardrail gaps:
   - Add richer phase-level trace logging fields.
   - Add explicit role/tool I/O attribution for post-run analysis.
2. Improve role scaffolding in `state/role_io_templates.py`:
   - Tighten template contract placeholders for phase constraints.
   - Add explicit machine-checkable sections to reduce parser drift.
3. Expand deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py`:
   - Add mode(s) that validate new trace schema and role I/O shape.
   - Ensure failing modes provide bounded, actionable diagnostics.
4. Wire evaluation checks:
   - Extend applicable guards in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` to detect schema regressions.
   - Confirm expected signal continuity in `state/metrics.json` outputs.
5. Validate incrementally:
   - `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`
   - Targeted `uv run python state/kernel.py --chapter-id <id>` dry run against deterministic checks.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Optional focused tests under `state/` matching new guards
