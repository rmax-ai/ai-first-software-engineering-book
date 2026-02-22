# Risks and decisions

## Risks discovered
- Planning-only output can drift from actual implementation constraints if follow-on iterations skip validation against current kernel behavior.
- Expanding observability may increase log volume; guardrails should enforce deterministic, bounded output.

## Decisions and trade-offs
- Chose to defer code edits and focus on an implementation-ready backlog, per seed-iteration instructions.
- Kept scope constrained to harness internals and eval contracts to avoid unrelated refactors.

## Intentionally deferred
- Any direct modifications to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
