# Risks and Decisions

## Risks
- Planning artifacts can drift from actual harness constraints if later iterations skip `DEVELOPMENT.md` and eval contract checks.
- Metric/eval coupling changes may require synchronized updates across `state/` and `evals/` to avoid false regression signals.

## Decisions and trade-offs
- Chose a planning-only iteration to satisfy the seed requirement and reduce risk of premature implementation churn.
- Kept backlog recommendations concrete (file-level targets) rather than broad architecture proposals to improve execution predictability.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` are deferred to the next iteration.
