# Risks and Decisions

## Risks discovered
- Plan quality risk: backlog could be too broad for incremental execution.
- Regression risk: future kernel changes may alter deterministic behavior if eval mappings are not enforced.

## Decisions and trade-offs
- Chose a planning-only seed iteration to satisfy prompt requirements before touching runtime code.
- Kept backlog concise and file-targeted to support minimal future diffs.

## Intentionally deferred
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
