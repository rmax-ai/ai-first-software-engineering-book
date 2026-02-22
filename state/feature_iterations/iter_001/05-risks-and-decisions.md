# Risks and decisions

## Risks
- The plan assumes existing kernel abstractions can accept additional trace metadata without expanding public interfaces.
- New eval checks may become brittle if trace formats are not kept stable across iterations.

## Decisions and trade-offs
- Chose planning-only scope for this seed iteration to satisfy prompt requirements and avoid premature code churn.
- Chose deterministic, UV-runnable validation as the primary test strategy for future implementation iterations.

## Deferred
- Concrete schema for trace payloads in `state/kernel.py`.
- Exact smoke mode additions in `state/copilot_sdk_uv_smoke.py`.
- Final eval rule syntax updates in `evals/*.yaml`.
