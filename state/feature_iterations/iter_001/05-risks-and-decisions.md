# Risks and decisions

## Risks discovered
- The initial plan may under-specify edge cases in trace payload schemas until `state/kernel.py` is inspected in detail.
- Eval YAML changes can over-constrain iteration throughput if acceptance thresholds are tightened too early.

## Decisions made
- Prioritized observability and deterministic guardrails before broader refactors.
- Deferred implementation to future iterations to satisfy the seed iteration planning requirement.

## Deferred intentionally
- Any code edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
