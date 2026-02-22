# Risks and decisions

## Risks discovered
- Planning-only output can drift from actual code constraints if follow-up slices are too large.
- Trace and role-template changes may affect multiple deterministic guards simultaneously.

## Decisions and trade-offs
- Chose a narrowly scoped seed backlog to keep follow-up iterations small and verifiable.
- Deferred implementation to preserve the prompt contract for this first iteration.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
