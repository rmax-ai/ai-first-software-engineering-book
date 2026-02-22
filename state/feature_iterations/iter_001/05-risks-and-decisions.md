# Risks and Decisions

## Risks discovered
- The backlog is documentation-first; implementation risk remains until kernel and smoke updates are executed.
- Eval mapping may still require minor schema adjustments once concrete trace fields are introduced.

## Decisions made
- Chose the smallest allowed scope: planning-only seed iteration with no harness code edits.
- Prioritized deterministic observability/testability items first to reduce regression risk in later iterations.

## Deferred intentionally
- Any modifications to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` are deferred to the next iteration task.
