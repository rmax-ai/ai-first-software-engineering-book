# Risks and Decisions

## Risks discovered
- Planning quality depends on future iterations preserving deterministic behavior and eval compatibility.
- Expanding observability in `state/kernel.py` can add output churn if metrics contracts are not updated in lockstep.

## Decisions made
- Keep this iteration planning-only to minimize risk and establish an auditable backlog.
- Prioritize kernel observability before role-IO/eval expansion so downstream tests target stable signals.

## Deferred intentionally
- Any implementation changes to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
