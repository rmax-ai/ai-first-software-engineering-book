# Next Iteration Recommendation

## Recommended next task
Implement deterministic trace-summary telemetry expansion in `state/kernel.py`.

## Why this is next
- It delivers immediate observability gains and creates clear signals for later smoke/eval tightening.

## Acceptance criteria
- Add structured trace-summary fields for phase outcomes and guard decisions without changing public CLI behavior.
- Add/adjust targeted harness tests or smoke assertions that validate new trace fields.
- Record validation evidence using `uv run python state/copilot_sdk_uv_smoke.py` and one focused kernel invocation.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`

