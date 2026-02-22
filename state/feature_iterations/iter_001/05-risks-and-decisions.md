# Risks and Decisions

## Risks discovered
- Planning quality risk: without concrete acceptance checks, future iterations could drift into broad refactors.
- Coverage risk: feature changes in `state/kernel.py` may outpace deterministic smoke coverage if `state/copilot_sdk_uv_smoke.py` is not expanded in lockstep.

## Decisions and trade-offs
- Decision: keep this iteration planning-only, as mandated by the seed-iteration guidance.
- Decision: prioritize observability and deterministic controls before broader behavior changes to reduce debugging cost.
- Trade-off: no executable harness code changes this iteration, so runtime behavior is unchanged until next iteration.

## Deferred intentionally
- Implementing trace logging in `state/kernel.py`.
- Updating templates in `state/role_io_templates.py`.
- Adding/adjusting smoke and eval artifacts in `state/copilot_sdk_uv_smoke.py` and `evals/*.yaml`.
