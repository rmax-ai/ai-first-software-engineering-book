# Risks and decisions

## Risks discovered
- The planning-only iteration cannot prove runtime behavior changes until follow-up implementation and UV-based smoke execution happen.
- Future edits in `state/kernel.py` could accidentally broaden scope without strict acceptance criteria.

## Decisions and trade-offs
- Chose a planning-first iteration to satisfy prompt seed requirements and minimize premature code churn.
- Prioritized deterministic harness controls, observability, and eval alignment to reduce regression risk before feature implementation.

## Intentionally deferred
- Direct code edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` are deferred to the next iteration task.
