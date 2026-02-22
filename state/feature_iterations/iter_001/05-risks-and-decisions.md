# Risks and Decisions

## Risks discovered

1. Planned feature additions to `state/kernel.py` could unintentionally alter deterministic behavior if trace/event schemas drift.
2. Expanding smoke modes in `state/copilot_sdk_uv_smoke.py` can increase maintenance cost unless table-driven patterns are preserved.
3. Eval updates under `evals/*.yaml` may create false negatives if not aligned with stable metrics outputs.

## Decisions made

1. Keep this iteration planning-only to satisfy the seed requirement with no runtime behavior changes.
2. Prioritize a single next implementation task with narrow scope and explicit acceptance criteria.
3. Anchor future changes to existing eval contracts before adding new gates.

## Deferred intentionally

- Actual code edits in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` are deferred to the next iteration.
