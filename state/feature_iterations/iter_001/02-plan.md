# Iteration plan

1. Inspect harness development guidance in `DEVELOPMENT.md` and align the backlog to UV-based execution and deterministic guardrails.
2. Define **feature track** for `state/kernel.py` and `state/role_io_templates.py`:
   - Add richer trace markers for loop phases and budget decisions in `state/kernel.py`.
   - Tighten role I/O templates in `state/role_io_templates.py` so role outputs are easier to validate deterministically.
3. Define **test track** for `state/copilot_sdk_uv_smoke.py` and adjacent harness checks:
   - Add focused smoke modes that exercise the new trace and role-template controls.
   - Keep deterministic mode coverage explicit and table-driven where possible.
4. Define **evaluation track** for `evals/*.yaml`:
   - Map new trace and template expectations to specific eval gates.
   - Require measurable signals (ledger/metrics deltas or explicit eval assertions) to detect regressions.
5. Break execution into smallest slices: first trace visibility, then role-template constraints, then smoke/eval wiring.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
