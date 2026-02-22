# Risks and Decisions

## Risks
- Planning-only iteration could drift if next task is too broad.
- Existing eval contracts may require tighter mapping once implementation begins.

## Decisions and trade-offs
- Chose a strictly planning scope to satisfy the seed prompt and avoid premature code churn.
- Prioritized deterministic harness verification paths (`uv run python ...`) over speculative new tooling.

## Deferred intentionally
- No changes to `state/kernel.py`, templates, smoke scripts, or eval YAMLs in this iteration.
- Detailed acceptance thresholds for new traces/evals deferred to the implementation iteration.
