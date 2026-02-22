# Risks and decisions

## Risks
- The backlog is concise by design, so implementation iterations must avoid scope creep when converting plan bullets into code changes.
- Eval coupling can regress if new harness signals are added without updating matching `evals/*.yaml` expectations.

## Decisions and trade-offs
- Chose a planning-only seed iteration to satisfy prompt requirements and minimize risk.
- Deferred all runtime modifications to future iterations so evidence can be gathered with targeted tests per feature.

## Intentionally deferred
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
