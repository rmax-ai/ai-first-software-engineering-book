# Risks and decisions

## Risks
- Planning may under-specify implementation details for telemetry schema changes in `state/kernel.py`.
- Eval contract updates can drift from real harness signals if `state/metrics.json` shape changes without synchronized eval edits.

## Decisions and trade-offs
- Kept scope strictly to planning artifacts to satisfy seed iteration constraints.
- Deferred implementation details to next iteration to avoid speculative code churn.

## Deferred items
- Concrete telemetry field additions in `state/kernel.py`.
- New/expanded smoke assertions in `state/copilot_sdk_uv_smoke.py`.
- Any `evals/*.yaml` threshold or rule adjustments.
