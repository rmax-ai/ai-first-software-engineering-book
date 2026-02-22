# Risks and decisions

## Risks
- Planning quality depends on current harness assumptions; future code inspection may refine ordering.
- Eval mapping may need adjustment if eval schemas evolve.

## Decisions and trade-offs
- Chose a planning-only iteration per prompt seed requirement; no code changes this round.
- Prioritized deterministic observability and verification-first sequencing over broad design expansion.

## Deferred intentionally
- Implementation in `state/kernel.py` and related files is deferred to the next iteration.
