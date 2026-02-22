# Risks and decisions

## Risks discovered
- Future kernel observability additions could increase log noise unless scoped to deterministic, parseable fields.
- Expanding smoke matrices can lengthen feedback cycles if scenarios are not prioritized.
- Eval contract edits in `evals/*.yaml` may introduce false failures if acceptance signals are not aligned with harness outputs.

## Decisions and trade-offs
- Chose a planning-only iteration, matching seed guidance, instead of implementing code changes immediately.
- Prioritized explicit feature→test→eval mapping to reduce ambiguity for the next iteration.
- Deferred implementation details to keep this iteration minimal and fully compliant with the one-task contract.

## Intentionally deferred
- Direct code edits in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
- Any changes to eval YAML files until the first implementation task is executed.
