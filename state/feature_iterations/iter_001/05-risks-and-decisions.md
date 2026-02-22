# Risks and Decisions

## Risks discovered
- Planning quality risk: future implementation may drift if backlog items are not tightly scoped per iteration.
- Verification risk: kernel/eval changes can introduce regressions if deterministic smoke and eval checks are not run together.

## Decisions and trade-offs
- Decision: keep this seed iteration planning-only, as required by prompt.
  - Trade-off: no immediate behavior improvement, but stronger execution guidance for subsequent iterations.
- Decision: anchor proposed verification commands to UV-managed runtime (`uv run python ...`) from `DEVELOPMENT.md`.
  - Trade-off: assumes existing runtime setup is available in later iterations.

## Deferred intentionally
- Any direct modifications to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` were deferred to future implementation iterations.
