# Task

## Selected task title
Add deterministic malformed `phase_trace` smoke coverage in `state/copilot_sdk_uv_smoke.py`.

## Why this task now
`state/feature_iterations/iter_056/06-next-iteration.md` prioritized protecting trace observability against schema drift in `phase_trace` payloads.

## Acceptance criteria
1. Add at least one deterministic malformed `phase_trace` validation path and assert expected failure behavior.
2. Keep existing `--mode trace-summary` success behavior green.
3. Record success-path and malformed-path validation evidence in this iteration.
