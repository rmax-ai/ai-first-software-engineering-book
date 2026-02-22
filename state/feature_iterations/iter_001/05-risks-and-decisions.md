# Risks and decisions

## Risks discovered
- Planning-only iteration does not yet prove runtime behavior changes in `state/kernel.py`.
- Future eval updates may require balancing strictness with false-positive risk in `evals/*.yaml`.
- Smoke expansion in `state/copilot_sdk_uv_smoke.py` can grow mode matrix cost if not kept table-driven.

## Decisions and trade-offs
- Chose a planning-first iteration exactly as required by the seed prompt.
- Kept scope to minimal markdown artifacts to avoid unrequested code churn.
- Prioritized deterministic trace-summary validation as the first implementation step because it provides high regression signal quickly.

## Deferred intentionally
- Direct code edits to `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
- Any change to eval YAML contracts until a concrete feature patch is implemented and test evidence is available.
