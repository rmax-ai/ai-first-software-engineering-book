# Risks and decisions

## Risks discovered
- Plan-level artifacts can drift from actual harness behavior if future iterations skip targeted smoke/eval checks.
- Adding new trace/eval guards may create false positives unless schemas remain stable and explicit.

## Decisions and trade-offs
- Chose a planning-only iteration to match the seed contract exactly, deferring all code edits.
- Prioritized deterministic observability + guardrails first, trading short-term feature delivery for safer subsequent implementation.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
