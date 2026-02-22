# Risks and Decisions

## Risks
- Planned scope may still be broad if a future iteration attempts multiple harness behaviors at once.
- Eval mappings may drift if implementation lands without updating corresponding `evals/*.yaml` assertions.

## Decisions and trade-offs
- Chose planning-only execution for this seed iteration to match prompt requirements and minimize risk.
- Deferred implementation details in favor of one concrete next task to keep iteration granularity tight.

## Deferred items
- Actual kernel/role-IO/smoke/eval code updates are intentionally deferred to the next iteration.
