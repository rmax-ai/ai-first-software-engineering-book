# Risks and Decisions

## Risks discovered
- Plan quality depends on later iterations preserving strict one-task scope.
- Harness behavior changes may require synchronized updates across kernel logic, smoke suites, and eval contracts.

## Decisions made
- Chose a planning-only seed iteration per prompt instructions.
- Prioritized deterministic observability and validation coverage before new behavior rollout.
- Structured next tasks as minimal, independently verifiable slices.

## Deferred intentionally
- Any implementation in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
- Any broad refactor not directly tied to the first planned implementation slice.
