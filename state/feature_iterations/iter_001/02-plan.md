# Plan

1. Baseline and observability hardening in `state/kernel.py`
   - Add structured phase/event trace summaries with stable keys.
   - Add explicit budget/guardrail decision logging for deterministic audits.
2. Role I/O contract tightening in `state/role_io_templates.py`
   - Normalize template constraints and required sections.
   - Add small validation helpers to fail fast on malformed role outputs.
3. Smoke coverage expansion in `state/copilot_sdk_uv_smoke.py`
   - Add targeted modes for new trace and validation behaviors.
   - Ensure mode matrix remains deterministic and table-driven.
4. Eval alignment in `evals/*.yaml`
   - Add or refine checks for new trace signals and role-output invariants.
   - Keep contracts explicit so regressions are surfaced by eval gates.
5. Verification scaffolding
   - Run `uv run python state/copilot_sdk_uv_smoke.py` with focused modes.
   - Run targeted kernel invocation(s) and compare expected trace/eval artifacts.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Focused test/harness assets under `state/` or `book/` as needed
