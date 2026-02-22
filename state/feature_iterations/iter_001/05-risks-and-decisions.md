# Risks and Decisions

## Risks
- Planning-only iteration does not validate runtime behavior changes yet.
- Future iterations may discover tighter coupling in `state/kernel.py` than expected.

## Decisions
- Chose planning scope only, per seed iteration instruction.
- Prioritized deterministic verification hooks (smoke + eval contracts) to reduce regression risk.

## Deferred
- Code implementation and test additions are deferred to the next iteration.
