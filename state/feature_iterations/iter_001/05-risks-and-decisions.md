# Risks and decisions

## Risks discovered
- Planning-only iterations can drift from real constraints if not tied to concrete validations.
- Future harness changes may unintentionally broaden scope across kernel, templates, and eval contracts in one pass.

## Decisions and trade-offs
- Chose strict seed scope: backlog planning only, with no production harness edits.
- Prioritized deterministic verification hooks in the backlog to reduce future ambiguity.

## Deferred intentionally
- Any implementation in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` is deferred to the next iteration.
