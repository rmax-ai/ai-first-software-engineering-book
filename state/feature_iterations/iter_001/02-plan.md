# Iteration plan

1. **Kernel observability and controls (`state/kernel.py`)**
   - Add structured phase-level trace metadata for decisions, guard outcomes, and budget use.
   - Add deterministic switches for strict mode behaviors (e.g., fail-fast on missing required artifacts).
   - Keep public CLI entry points stable while expanding internal telemetry payloads.

2. **Role I/O contract clarity (`state/role_io_templates.py`)**
   - Refine role templates so planner/writer/critic sections expose explicit required inputs/outputs.
   - Standardize template fields to reduce ambiguous model responses and downstream parsing variance.

3. **Harness smoke coverage (`state/copilot_sdk_uv_smoke.py`)**
   - Add or extend table-driven smoke modes that validate new trace metadata and strict-mode controls.
   - Ensure uv-driven execution remains deterministic and reports machine-checkable failure reasons.

4. **Eval alignment (`evals/*.yaml`)**
   - Map new harness signals to existing eval contracts (`chapter-quality.yaml`, `style-guard.yaml`, `drift-detection.yaml`).
   - Add focused assertions only where current evals cannot detect the planned regressions.

5. **Test harness assets**
   - Add/update fixtures under `state/` to exercise missing/invalid phase payloads and trace coverage paths.
   - Keep fixtures minimal and reusable across smoke and kernel-level tests.

## Expected files to change in future implementation iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/copilot_sdk_smoke_test.py` (if deterministic smoke matrix updates are needed)
