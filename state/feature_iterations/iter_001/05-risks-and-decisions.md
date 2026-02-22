# Risks and decisions

## Risks
- Planned kernel observability changes could increase log noise if not constrained to deterministic summaries.
- Smoke/eval expansions may fail if metric names drift from `state/metrics.json` conventions.

## Decisions and trade-offs
- Chose planning-only scope to honor seed-iteration requirement and avoid premature implementation churn.
- Kept backlog concrete (files, commands, acceptance criteria) so next iteration can execute one small task safely.

## Deferred items
- No implementation changes to Python modules in this iteration; deferred to next iteration task.
