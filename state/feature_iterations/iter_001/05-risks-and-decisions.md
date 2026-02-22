# Risks and decisions

## Risks
- Plan-level ambiguity may remain until concrete constraints in `state/kernel.py` are inspected during implementation.
- Future eval tightening in `evals/*.yaml` may fail existing flows if acceptance thresholds are set too aggressively.

## Decisions and trade-offs
- Chose strict planning-only scope to satisfy the seed-iteration requirement and avoid accidental behavior changes.
- Prioritized deterministic observability and role-IO clarity first, because these reduce debugging cost for later feature work.

## Deferred items
- Exact metric keys and trace payload schemas are deferred to the next implementation iteration.
- Any refactors outside the listed harness/eval surfaces are intentionally deferred.
