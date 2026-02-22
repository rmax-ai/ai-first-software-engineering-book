# Risks and Decisions

## Risks
- Planning artifacts can drift from actual harness constraints if not revalidated before implementation.
- Eval contract changes may require updates across multiple YAML files, increasing coordination cost.

## Decisions
- Kept this iteration strictly planning-only per seed-iteration contract.
- Deferred all code changes to the next iteration to preserve minimal scope and clear evidence.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
