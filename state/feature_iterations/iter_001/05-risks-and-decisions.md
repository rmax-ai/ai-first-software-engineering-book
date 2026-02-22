# Risks and decisions

## Risks discovered
- Planning quality depends on assumptions until implementation validates feasibility.
- Trace/logging expansion in `state/kernel.py` may increase output noise if not scoped.
- New eval constraints may cause false positives if signals are underspecified.

## Decisions and trade-offs
- Chose a planning-only first iteration to reduce implementation risk.
- Prioritized deterministic observability and contract validation before broader features.
- Limited scope to one backlog seed and one concrete next task for clean handoff.

## Deferred intentionally
- Any runtime code edits in `state/` and `evals/` deferred to next iteration.
