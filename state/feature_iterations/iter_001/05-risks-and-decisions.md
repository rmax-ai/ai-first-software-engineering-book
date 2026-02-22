# Risks and Decisions

## Risks
- Planning-only output can drift from current code if follow-up iterations are delayed.
- Expanded smoke/eval coverage may increase runtime and require careful scoping.

## Decisions and trade-offs
- Chose a minimal, execution-ready backlog instead of speculative implementation details.
- Deferred code edits to keep this iteration aligned with the seed requirement.

## Deferred intentionally
- Any direct changes to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.

